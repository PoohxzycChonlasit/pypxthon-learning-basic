# Data Analysis Practice Track

This optional, offline track adds practical data work after the standard-library foundations in Levels 1–5. It includes CSV, JSON and SQLite ingestion, data validation, NumPy, pandas, Matplotlib, business analytics and synthetic financial data. All market-like values are generated for practice and are not historical prices.

## Start and open the exercises

Open the project folder in VS Code, then open the named exercise module under `tracks/data_analysis/exercises/`. Each module contains a UTF-8 instruction box with the objective, scenario, input/output, syntax focus and TODO location. Detailed Thai explanations are in `explanations/`; three hints per exercise are in `hints/`; reference code is in `solutions/`.

Start with DA01 and do DA01–DA05 before the package-dependent exercises:

~~~powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
code .
~~~

| ID | Topic | Dependency | Difficulty |
|---|---|---|---|
| DA01–DA05 | Dataset/schema profile, CSV, JSON, SQLite, validation and rejected-row ledger | Standard library | Tiers 1–5 |
| DA06–DA09 | NumPy arrays, indexing/slicing, broadcasting, aggregation and statistics | NumPy | Tiers 1–4 |
| DA10–DA17 | Series/DataFrame, read_csv, head/info/describe, loc/iloc, cleaning, groupby/merge, time series and EDA | pandas + NumPy | Tiers 1–5 |
| DA18–DA19 | Business charts and validated synthetic OHLCV price/volume charts | Matplotlib + pandas | Tiers 4–5 |
| DA20–DA21 | Business KPIs, returns, costs, equity curve and drawdown | pandas + NumPy | Tiers 4–5 |
| DA22 | UTF-8 CSV report export and round-trip check | pandas | Tier 2 |
| DA23 | Interactive conversion chart (optional extension) | Plotly + pandas | Optional Tier 3 |

The `difficulty_tier` is relative to this track: Tier 1 introduces one idea; Tier 2 combines familiar ideas; Tier 3 uses several steps; Tier 4 handles data-quality and boundary conditions; Tier 5 transfers concepts to a new analysis problem.

This track is intentionally optional: it adds package practice without changing the stable 150-exercise core IDs. It provides genuine graded NumPy and pandas tasks and hands-on charting. The existing core Levels 1–10 still introduce statistics, risk and offline quant research; this track supplies more depth in data ingestion and analytics.

## Check an exercise

The grade files check the student's exercise module against fixed expectations. A failure is expected until the corresponding TODO is completed. For example, check the standard-library tasks first:

~~~powershell
python -B -m unittest discover -s tracks/data_analysis/tests -p grade_foundations.py -v
~~~

To run only DA03, add `-k DA03`. The test cases are handwritten and do not calculate their expected values by running the reference solution.

## Optional packages

Levels 1–5 and DA01–DA05 require only Python 3.12's standard library. For DA06–DA22, use the project-local `.venv` with NumPy, pandas and Matplotlib; Plotly is only needed for DA23. Keep these packages out of global Python. Get approval from the project owner before installing optional dependencies.

~~~powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
python -B -m venv .venv
~~~

After approval, install into this environment only:

~~~powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-optional.txt
~~~

Then select `.venv\Scripts\python.exe` in VS Code and run package graders:

~~~powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s tracks/data_analysis/tests -p grade_numpy_pandas.py -v
.\.venv\Scripts\python.exe -B -m unittest discover -s tracks/data_analysis/tests -p grade_visualization.py -v
.\.venv\Scripts\python.exe -B -m unittest discover -s tracks/data_analysis/tests -p grade_capstone.py -v
~~~

DA23 is optional and has its own test file. Matplotlib tests use the noninteractive `Agg` backend and inspect chart data, labels and saved files rather than relying on pixel comparisons.

## Data and safety

Use [the synthetic dataset guide](../../data/README.md) and regenerate fixtures with `python -B data/generate_synthetic_datasets.py`. The clean OHLCV files have positive prices, nonnegative volume, ordered unique timestamps and valid high/low relationships. Gaps in dates are intentional. Invalid rows live only in the separate dirty e-commerce fixture. No task connects to an exchange, wallet, broker or live trading service.
