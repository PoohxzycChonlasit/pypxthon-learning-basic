# Hints — NumPy practice

## DA06 — Create an array

1. Convert the input once into a NumPy array with a numeric dtype.
2. Confirm the result is one-dimensional; an empty one-dimensional array is valid.
3. A float dtype keeps integer and decimal inputs consistent for later calculations.

## DA07 — Index and slice

1. The OHLC close column is index 3 because row positions start at zero.
2. Combine row slicing and column selection in one NumPy index expression.
3. Return a copy so changing the result cannot change the original matrix.

## DA08 — Vectorization and broadcasting

1. Compare matrix shape `(rows, columns)` with the weight vector length.
2. NumPy can apply a column-sized vector to every row without a Python loop.
3. Verify both the first and last weighted values and confirm the source matrix is unchanged.

## DA09 — Aggregation

1. Convert to a one-dimensional finite numeric array and reject empty input.
2. Use NumPy's sum, mean, minimum and maximum reductions.
3. Population standard deviation uses `ddof=0`; sample standard deviation uses `ddof=1`.
