"""Reference implementations for pandas practice."""

from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd


def series_profile(values):
    series = pd.Series(values, dtype="float64")
    clean = series.dropna()
    return {
        "count": int(clean.size),
        "missing": int(series.isna().sum()),
        "mean": None if clean.empty else float(clean.mean()),
        "median": None if clean.empty else float(clean.median()),
    }


def csv_overview(path):
    frame = pd.read_csv(path)
    buffer = StringIO()
    frame.info(buf=buffer)
    describe = frame.describe(include="all").to_dict()
    return {
        "columns": list(frame.columns),
        "shape": tuple(frame.shape),
        "head": frame.head().to_dict(orient="records"),
        "info": buffer.getvalue(),
        "describe": describe,
    }


def filter_sort_sales(path, category, minimum_revenue):
    frame = pd.read_csv(path)
    frame["revenue"] = pd.to_numeric(frame["quantity"]) * pd.to_numeric(frame["unit_price"])
    selected = frame.loc[(frame["category"] == category) & (frame["revenue"] >= minimum_revenue)]
    selected = selected.sort_values(["revenue", "order_id"], ascending=[False, True])
    columns = [selected.columns.get_loc(name) for name in ("order_id", "product", "revenue")]
    return selected.iloc[:, columns].to_dict(orient="records")


def clean_event_csv(path):
    frame = pd.read_csv(path, dtype="string", keep_default_na=False)
    accepted = []
    rejected = []
    seen = set()
    for row in frame.to_dict(orient="records"):
        event_id = row.get("event_id", "")
        reason = None
        timestamp = pd.to_datetime(row.get("timestamp", ""), errors="coerce", utc=True)
        value = pd.to_numeric(row.get("value", ""), errors="coerce")
        if not event_id:
            reason = "missing event_id"
        elif event_id in seen:
            reason = "duplicate event_id"
        elif pd.isna(timestamp):
            reason = "invalid timestamp"
        elif pd.isna(value):
            reason = "invalid value"
        elif not np.isfinite(value):
            reason = "value must be finite"
        elif value < 0:
            reason = "value must be nonnegative"
        seen.add(event_id)
        if reason:
            rejected.append({"event_id": event_id or None, "reason": reason})
        else:
            accepted.append({"event_id": event_id, "timestamp": timestamp.isoformat(), "value": float(value)})
    return {"accepted": accepted, "rejected": rejected}


def sales_by_category(transactions_path, products_path):
    transactions = pd.read_csv(transactions_path)
    products = pd.read_csv(products_path)
    joined = transactions.merge(products, on="product_id", how="left", validate="many_to_one", indicator=True)
    if (joined["_merge"] != "both").any():
        raise ValueError("transaction contains an unknown product_id")
    joined["revenue"] = joined["quantity"] * joined["unit_price"]
    summary = joined.groupby("category", as_index=False).agg(
        order_count=("transaction_id", "count"), revenue=("revenue", "sum")
    )
    summary["revenue"] = summary["revenue"].round(2)
    return summary.sort_values("category").to_dict(orient="records")


def daily_price_features(path, window=3):
    if window < 2:
        raise ValueError("window must be at least 2")
    frame = pd.read_csv(path, parse_dates=["timestamp"])
    if frame["timestamp"].duplicated().any():
        raise ValueError("timestamps must be unique")
    frame = frame.sort_values("timestamp").set_index("timestamp")
    daily = frame["close"].resample("D").last()
    return pd.DataFrame(
        {
            "close": daily,
            "lag_close": daily.shift(1),
            "pct_change": daily.pct_change(fill_method=None),
            "rolling_mean": daily.rolling(window=window, min_periods=window).mean(),
        }
    )


def time_based_split(frame, timestamp_column, split_timestamp):
    result = frame.copy()
    result[timestamp_column] = pd.to_datetime(result[timestamp_column], errors="raise", utc=True)
    split = pd.to_datetime(split_timestamp, errors="raise", utc=True)
    result = result.sort_values(timestamp_column, kind="stable")
    train = result.loc[result[timestamp_column] < split].copy()
    test = result.loc[result[timestamp_column] >= split].copy()
    return train, test


def eda_summary(path, value_column, comparison_column, category_column, date_column):
    frame = pd.read_csv(path)
    values = pd.to_numeric(frame[value_column], errors="coerce")
    comparison = pd.to_numeric(frame[comparison_column], errors="coerce")
    clean = values.dropna()
    q1, q3 = clean.quantile([0.25, 0.75])
    iqr = q3 - q1
    outliers = int(((clean < q1 - 1.5 * iqr) | (clean > q3 + 1.5 * iqr)).sum())
    corr_frame = pd.concat([values, comparison], axis=1).dropna()
    correlation = None if corr_frame.nunique().min() < 2 else float(corr_frame.corr().iloc[0, 1])
    dated = frame.assign(_date=pd.to_datetime(frame[date_column], errors="coerce"))
    trend = dated.dropna(subset=["_date"]).groupby(dated["_date"].dt.to_period("M"))[value_column].sum()
    distribution = values.value_counts(bins=4, sort=False).tolist() if len(clean) else []
    category_means = frame.assign(_value=values).groupby(category_column)["_value"].mean().sort_index()
    return {
        "rows": int(len(frame)),
        "missing_cells": int(frame.isna().sum().sum()),
        "duplicate_rows": int(frame.duplicated().sum()),
        "description": {
            "mean": float(clean.mean()) if len(clean) else None,
            "median": float(clean.median()) if len(clean) else None,
            "min": float(clean.min()) if len(clean) else None,
            "max": float(clean.max()) if len(clean) else None,
        },
        "distribution_counts": [int(value) for value in distribution],
        "category_means": {str(key): float(value) for key, value in category_means.items()},
        "monthly_trend": {str(key): float(value) for key, value in trend.items()},
        "outlier_count_iqr": outliers,
        "correlation": correlation,
    }


def export_analysis(frame, output_path):
    path = Path(output_path)
    frame.to_csv(path, index=False, encoding="utf-8")
    return {"path": str(path), "rows": int(len(frame))}
