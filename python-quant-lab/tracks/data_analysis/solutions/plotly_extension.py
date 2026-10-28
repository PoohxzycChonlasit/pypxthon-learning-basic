"""Reference implementation for the optional Plotly extension."""

from pathlib import Path

import pandas as pd
import plotly.express as px


def interactive_conversion_chart(path, html_output_path):
    frame = pd.read_csv(path, parse_dates=["date"])
    daily = frame.groupby(["date", "channel"], as_index=False)[["sessions", "conversions"]].sum()
    daily["conversion_rate"] = daily["conversions"] / daily["sessions"].where(daily["sessions"] > 0)
    figure = px.line(
        daily,
        x="date",
        y="conversion_rate",
        color="channel",
        labels={"date": "Date", "conversion_rate": "Conversion rate", "channel": "Channel"},
    )
    figure.write_html(Path(html_output_path), include_plotlyjs=True)
    return figure
