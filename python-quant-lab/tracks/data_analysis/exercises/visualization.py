"""Matplotlib exercises DA18–DA19; figures are tested via data and labels."""

import matplotlib.pyplot as plt
import pandas as pd


# ┌─ DA18 · Line, bar, histogram and scatter charts ─────────────────────────
# │ Tier 4 · Matplotlib · Use synthetic website_sessions.csv.
# │ Objective: build four charts that answer different questions.
# │ Scenario: a business analyst compares channel trends and conversion data.
# │ Input: CSV with date, channel, sessions and conversions; output: Figure.
# │ Syntax: subplots(); plot(); bar(); hist(); scatter(); set_xlabel().
# │ ☐ line for trend  ☐ bar for category totals  ☐ histogram for distribution
# │ ☐ scatter for two numeric variables; assert labels and plotted data in tests
# │ TODO: implement business_charts. Save/inspect the artifact as shown in
# │ README.
# │ Hint/solution: ../hints/visualization.md / ../solutions/visualization.py
# └───────────────────────────────────────────────────────────────────────────
def business_charts(path):
    raise NotImplementedError


# ┌─ DA19 · Synthetic OHLCV price and volume chart ──────────────────────────
# │ Tier 5 · Matplotlib · Never call this fixture historical market data.
# │ Objective: validate ordered, finite OHLCV rows and save close/range/volume charts.
# │ Scenario: a Quant researcher reviews a synthetic offline price series.
# │ Input: synthetic OHLCV CSV and output image path; output: Figure.
# │ Syntax: fill_between(low, high); plot(close); bar(timestamp, volume).
# │ ☐ reject invalid OHLC relationships or duplicate timestamps
# │ ☐ verify axis labels, plotted values and nonempty saved artifact
# │ TODO: implement ohlcv_chart. Tests: see track README.
# │ Hint/solution: ../hints/visualization.md / ../solutions/visualization.py
# └───────────────────────────────────────────────────────────────────────────
def ohlcv_chart(path, output_path):
    raise NotImplementedError
