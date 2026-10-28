"""NumPy exercises DA06–DA09. Run only in the project .venv after approval."""

import numpy as np


# ┌─ DA06 · Create a numeric array ──────────────────────────────────────────
# │ Tier 1 · NumPy · After Level 5 and DA01–DA05.
# │ Objective: make a one-dimensional float array from numeric input.
# │ Scenario: an analyst prepares a numeric price column for calculation.
# │ Input: list of numbers; output: ndarray with shape (n,) and float dtype.
# │ Syntax: np.asarray(values, dtype=float); array.shape; array.dtype.
# │ ☐ preserve order  ☐ support an empty list  ☐ do not edit the input list
# │ Example: [2, 5] -> array([2.0, 5.0])
# │ TODO: implement make_price_array. Tests: see track README.
# │ Hint/solution: ../hints/numpy_practice.md / ../solutions/numpy_practice.py
# └───────────────────────────────────────────────────────────────────────────
def make_price_array(values):
    raise NotImplementedError


# ┌─ DA07 · Index and slice an OHLC matrix ──────────────────────────────────
# │ Tier 2 · NumPy · Input columns are open, high, low, close.
# │ Objective: select close prices for the half-open row range [start:stop].
# │ Scenario: a researcher extracts one price column for a defined time window.
# │ Input: 2-D numeric array, start and stop; output: a 1-D close-price array.
# │ Syntax: matrix[start:stop, column]; index begins at zero and stop is
# │ excluded.
# │ ☐ keep requested row order  ☐ allow an empty slice  ☐ return an
# │ independent array
# │ Example: [[1,2,0,1.5],[2,3,1,2.5]], 0, 1 -> [1.5]
# │ TODO: implement select_close_window. Tests: see track README.
# │ Hint/solution: ../hints/numpy_practice.md / ../solutions/numpy_practice.py
# └───────────────────────────────────────────────────────────────────────────
def select_close_window(ohlc, start, stop):
    raise NotImplementedError


# ┌─ DA08 · Vectorized calculation and broadcasting ────────────────────────
# │ Tier 3 · NumPy · Each row is an item; each column is a feature.
# │ Objective: multiply each matrix column by its matching weight.
# │ Scenario: a data scientist applies one conversion factor per measurement.
# │ Input: matrix shape (rows, columns), weights shape (columns,).
# │ Output: new array with the same shape; NumPy broadcasting is required.
# │ Syntax: matrix * weights broadcasts weights across rows.
# │ ☐ avoid Python loops  ☐ do not mutate the source matrix
# │ Example: [[2,3],[4,5]] * [10,100] -> [[20,300],[40,500]]
# │ TODO: implement apply_column_weights. Tests: see track README.
# │ Hint/solution: ../hints/numpy_practice.md / ../solutions/numpy_practice.py
# └───────────────────────────────────────────────────────────────────────────
def apply_column_weights(values, weights):
    raise NotImplementedError


# ┌─ DA09 · Aggregate and summarize numeric data ────────────────────────────
# │ Tier 4 · NumPy · Statistics are population statistics for this exercise.
# │ Objective: return sum, mean, standard deviation, minimum and maximum.
# │ Scenario: an analyst produces a deterministic numeric quality summary.
# │ Input: nonempty one-dimensional numeric sequence; output: a named
# │ dictionary.
# │ Syntax: np.mean, np.std(ddof=0), np.min and np.max.
# │ ☐ use population standard deviation  ☐ preserve float precision
# │ Example: [2,4,6] -> mean 4, standard deviation sqrt(8/3)
# │ TODO: implement numeric_summary. Tests: see track README.
# │ Hint/solution: ../hints/numpy_practice.md / ../solutions/numpy_practice.py
# └───────────────────────────────────────────────────────────────────────────
def numeric_summary(values):
    raise NotImplementedError
