"""Reference implementations for deterministic Matplotlib chart exercises."""

import math

import matplotlib.pyplot as plt
import pandas as pd


def business_charts(path):
    frame = pd.read_csv(path, parse_dates=["date"])
    daily = frame.groupby("date", as_index=False)["sessions"].sum().sort_values("date")
    by_channel = frame.groupby("channel", as_index=False)[["sessions", "conversions"]].sum()
    figure, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)
    axes[0, 0].plot(daily["date"], daily["sessions"])
    axes[0, 0].set(title="Daily sessions", xlabel="Date", ylabel="Sessions")
    axes[0, 1].bar(by_channel["channel"], by_channel["sessions"])
    axes[0, 1].set(title="Sessions by channel", xlabel="Channel", ylabel="Sessions")
    axes[1, 0].hist(frame["sessions"], bins=10)
    axes[1, 0].set(title="Session distribution", xlabel="Sessions per channel/day", ylabel="Count")
    axes[1, 1].scatter(frame["sessions"], frame["conversions"])
    axes[1, 1].set(title="Sessions and conversions", xlabel="Sessions", ylabel="Conversions")
    return figure


def ohlcv_chart(path, output_path):
    frame = pd.read_csv(path, parse_dates=["timestamp"])
    if frame["timestamp"].duplicated().any() or not frame["timestamp"].is_monotonic_increasing:
        raise ValueError("timestamps must be unique and ordered")
    numeric = frame[["open", "high", "low", "close", "volume"]].astype(float)
    if not all(math.isfinite(float(value)) for value in numeric.to_numpy().ravel()):
        raise ValueError("prices and volume must be finite")
    if (numeric[["open", "high", "low", "close"]] <= 0).any().any() or (numeric["volume"] < 0).any():
        raise ValueError("prices must be positive and volume nonnegative")
    if (numeric["high"] < numeric[["open", "close"]].max(axis=1)).any():
        raise ValueError("high is below open or close")
    if (numeric["low"] > numeric[["open", "close"]].min(axis=1)).any() or (numeric["low"] > numeric["high"]).any():
        raise ValueError("low/high relationship is invalid")
    figure, (price_axis, volume_axis) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    price_axis.fill_between(frame["timestamp"], numeric["low"], numeric["high"], alpha=0.18, label="Low–High range")
    price_axis.plot(frame["timestamp"], numeric["close"], label="Close")
    price_axis.set_ylabel("Synthetic price")
    price_axis.legend()
    volume_axis.bar(frame["timestamp"], numeric["volume"])
    volume_axis.set_xlabel("Timestamp")
    volume_axis.set_ylabel("Volume")
    figure.tight_layout()
    figure.savefig(output_path)
    return figure
