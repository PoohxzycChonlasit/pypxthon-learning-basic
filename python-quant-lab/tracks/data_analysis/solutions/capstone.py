"""Reference implementations for offline business and quantitative analysis."""

import numpy as np
import pandas as pd


def business_kpis(transactions_path, sessions_path, inventory_path):
    transactions = pd.read_csv(transactions_path)
    sessions = pd.read_csv(sessions_path)
    inventory = pd.read_csv(inventory_path)
    revenue = transactions["quantity"] * transactions["unit_price"] * (1 - transactions["discount_rate"])
    total_revenue = float(revenue.sum())
    order_count = int(len(transactions))
    session_count = int(sessions["sessions"].sum())
    conversion_count = int(sessions["conversions"].sum())
    segment_revenue = (
        transactions.assign(revenue=revenue).groupby("customer_segment")["revenue"].sum().sort_index()
    )
    sku_movement = inventory.groupby("sku")["quantity_delta"].sum().sort_index()
    return {
        "order_count": order_count,
        "total_revenue": round(total_revenue, 2),
        "average_order_value": round(total_revenue / order_count, 2) if order_count else 0.0,
        "conversion_rate": conversion_count / session_count if session_count else None,
        "revenue_by_segment": {str(key): round(float(value), 2) for key, value in segment_revenue.items()},
        "net_inventory_movement_by_sku": {str(key): int(value) for key, value in sku_movement.items()},
    }


def financial_metrics(prices, positions, fee_rate):
    prices = np.asarray(prices, dtype=float)
    positions = np.asarray(positions, dtype=float)
    if prices.ndim != 1 or prices.size < 2 or not np.isfinite(prices).all() or (prices <= 0).any():
        raise ValueError("prices must be a finite positive series with at least two values")
    if positions.shape != (prices.size - 1,) or not np.isin(positions, [-1, 0, 1]).all():
        raise ValueError("provide one {-1, 0, 1} position per forward return")
    if not np.isfinite(fee_rate) or fee_rate < 0 or fee_rate >= 1:
        raise ValueError("fee_rate must be between 0 and 1")
    simple_returns = prices[1:] / prices[:-1] - 1
    log_returns = np.log(prices[1:] / prices[:-1])
    gross_returns = simple_returns * positions
    costs = fee_rate * np.abs(positions)
    net_returns = gross_returns - costs
    if (net_returns <= -1).any():
        raise ValueError("costs create a total loss or worse")
    equity = np.cumprod(1 + net_returns)
    peaks = np.maximum.accumulate(np.concatenate(([1.0], equity)))[1:]
    drawdowns = equity / peaks - 1
    return {
        "simple_returns": simple_returns.tolist(),
        "log_returns": log_returns.tolist(),
        "net_returns": net_returns.tolist(),
        "equity_curve": equity.tolist(),
        "drawdowns": drawdowns.tolist(),
        "volatility": float(np.std(log_returns, ddof=0)),
        "max_drawdown": float(np.min(drawdowns)),
        "total_return": float(equity[-1] - 1),
    }
