# Hints — Data Analysis foundations

Hints progress from concepts to pseudocode. None contains a complete solution.

## DA01 — Dataset profile

1. A schema is the ordered set of keys in the first row. A duplicate row is a repeated record, not merely a repeated ID.
2. Build a stable marker from each row's key/value pairs and keep markers in a set.
3. Count only cells that are `None` or the empty string; a numeric zero is valid data.

## DA02 — CSV ingestion

1. CSV cells arrive as text. Do not convert values unless the task asks.
2. Use `csv.DictReader` in a `with open(..., encoding="utf-8", newline="")` block.
3. An empty file has no `fieldnames`; decide how to report that before reading rows.

## DA03 — JSON ingestion

1. JSON has several possible outer shapes; validate the shape before iterating.
2. Accept a list directly or read the `records` value from an object.
3. Require every item to be a dictionary and raise `ValueError` for any other shape.

## DA04 — SQLite monthly aggregation

1. SQLite is local and available in the Python standard library.
2. Group the sale date prefix `YYYY-MM`; sum `quantity * unit_price` per group.
3. Sort the SQL result by month and round the final revenue to two decimal places.

## DA05 — Transaction cleaning

1. Validate one row at a time and keep accepted and rejected output separate.
2. Parse date, integer quantity, price and discount; check ranges after conversion.
3. Track seen transaction IDs, preserve the input list, and record one clear rejection reason per row.
