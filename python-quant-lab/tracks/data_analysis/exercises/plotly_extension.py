"""Optional Plotly extension DA23; not required for the core track."""

import pandas as pd
import plotly.express as px


# ┌─ DA23 · Optional interactive conversion chart ───────────────────────────
# │ Optional Tier 3 · Plotly · Not part of the required package gate.
# │ Objective: compare synthetic daily sessions by marketing channel.
# │ Input: website_sessions.csv; output: Plotly Figure with labeled axes.
# │ Syntax: px.line(data_frame, x=..., y=..., color=...).
# │ ☐ leave conversion rate missing when sessions=0
# │ ☐ aggregate by date/channel  ☐ keep the source CSV unchanged
# │ ☐ verify trace names, values, axis labels and saved HTML artifact
# │ TODO: implement interactive_conversion_chart. See optional approval note.
# │ Hint/solution: README.md · reference: ../solutions/plotly_extension.py
# └───────────────────────────────────────────────────────────────────────────
def interactive_conversion_chart(path, html_output_path):
    raise NotImplementedError
