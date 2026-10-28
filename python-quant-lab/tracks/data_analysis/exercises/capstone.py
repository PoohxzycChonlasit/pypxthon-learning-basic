"""Business and financial analysis capstone exercises DA20–DA21."""

import numpy as np
import pandas as pd


# ┌─ DA20 · Business KPI report ─────────────────────────────────────────────
# │ Tier 4 · pandas/NumPy · Use only synthetic offline business datasets.
# │ Objective: report net revenue, orders, average order value, conversion,
# │ revenue by segment, and net inventory movement by SKU.
# │ Scenario: an operations team reviews sales, traffic and stock together.
# │ Input: transaction, session and inventory CSV paths; output: plain dict.
# │ Syntax: read_csv(); vectorized columns; groupby().sum(); merge().
# │ ☐ apply discount_rate as a fraction  ☐ handle zero sessions safely
# │ ☐ do not claim these KPIs prove causation or business performance
# │ TODO: implement business_kpis. Tests: see track README.
# │ Hint/solution: ../hints/capstone.md / ../solutions/capstone.py
# └───────────────────────────────────────────────────────────────────────────
def business_kpis(transactions_path, sessions_path, inventory_path):
    raise NotImplementedError


# ┌─ DA21 · Offline financial returns, costs and drawdown ───────────────────
# │ Tier 5 · NumPy · This is analysis only; no broker or exchange connection.
# │ Objective: compute simple/log returns, volatility, costs, equity and
# │ drawdown.
# │ Scenario: a researcher checks a paper-only rule on deterministic prices.
# │ Input: positive prices, one {-1,0,1} position per return, fee per exposure.
# │ Output: arrays/lists and summary metrics; never submit a real order.
# │ Syntax: np.diff/log/maximum.accumulate/cumprod and np.std(ddof=0).
# │ ☐ align signal with the next return  ☐ subtract fees  ☐ preserve time order
# │ ☐ report max drawdown as a nonpositive fraction
# │ TODO: implement financial_metrics. Tests: see track README.
# │ Hint/solution: ../hints/capstone.md / ../solutions/capstone.py
# └───────────────────────────────────────────────────────────────────────────
def financial_metrics(prices, positions, fee_rate):
    raise NotImplementedError
