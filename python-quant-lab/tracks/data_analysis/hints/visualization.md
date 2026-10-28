# Hints — charts and visual checks

## DA18 — Business charts

1. Aggregate daily totals and channel totals before drawing the line and bar charts.
2. A histogram shows a numeric distribution; a scatter plot shows paired numeric values.
3. Test axis labels and plotted data arrays rather than comparing rendered pixels.

## DA19 — OHLCV chart

1. Validate timestamp order, uniqueness, positive prices and nonnegative volume first.
2. Draw the low-to-high range behind the close line; show volume on a separate shared x-axis.
3. Save a figure to a temporary path, then check the file and line/label data.

## DA23 — Optional Plotly chart

1. Aggregate session and conversion counts by date and channel before dividing.
2. Set axis labels and color by channel so an interactive legend can filter traces.
3. Inspect trace names and values and verify the standalone HTML file was written.
