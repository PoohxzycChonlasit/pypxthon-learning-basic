"""Reference implementations for NumPy practice."""

import numpy as np


def make_price_array(values):
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError("expected one-dimensional input")
    return array


def select_close_window(ohlc, start, stop):
    matrix = np.asarray(ohlc, dtype=float)
    if matrix.ndim != 2 or matrix.shape[1] != 4:
        raise ValueError("expected columns open, high, low, close")
    if start < 0 or stop < start:
        raise ValueError("invalid row range")
    return matrix[start:stop, 3].copy()


def apply_column_weights(values, weights):
    matrix = np.asarray(values, dtype=float)
    factors = np.asarray(weights, dtype=float)
    if matrix.ndim != 2 or factors.ndim != 1 or matrix.shape[1] != factors.size:
        raise ValueError("weights must match matrix columns")
    return matrix * factors


def numeric_summary(values):
    array = np.asarray(values, dtype=float)
    if array.ndim != 1 or array.size == 0 or not np.isfinite(array).all():
        raise ValueError("expected nonempty finite one-dimensional values")
    return {
        "sum": float(np.sum(array)),
        "mean": float(np.mean(array)),
        "std": float(np.std(array, ddof=0)),
        "min": float(np.min(array)),
        "max": float(np.max(array)),
    }
