"""Optional Plotly grader; run only after separately approved installation."""

import sys
import tempfile
import unittest
from pathlib import Path


EXERCISES = Path(__file__).resolve().parents[1] / "exercises"
sys.path.insert(0, str(EXERCISES))
from plotly_extension import interactive_conversion_chart


class PlotlyOptionalTests(unittest.TestCase):
    def test_DA23_trace_labels_values_and_html(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "sessions.csv"
            source.write_text(
                "date,channel,sessions,conversions\n"
                "2025-01-01,email,100,10\n2025-01-01,email,50,5\n"
                "2025-01-01,search,200,10\n",
                encoding="utf-8",
            )
            output = folder / "chart.html"
            figure = interactive_conversion_chart(source, output)
            traces = {trace.name: list(trace.y) for trace in figure.data}
            self.assertEqual(set(traces), {"email", "search"})
            self.assertEqual(traces["email"], [0.1])
            self.assertEqual(traces["search"], [0.05])
            self.assertEqual(figure.layout.xaxis.title.text, "Date")
            self.assertEqual(figure.layout.yaxis.title.text, "Conversion rate")
            self.assertTrue(output.is_file())
            self.assertGreater(output.stat().st_size, 1000)

    def test_DA23_zero_sessions_remain_missing(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "sessions.csv"
            source.write_text("date,channel,sessions,conversions\n2025-01-01,email,0,0\n", encoding="utf-8")
            output = folder / "empty-rate.html"
            figure = interactive_conversion_chart(source, output)
            self.assertEqual(figure.data[0].name, "email")
            value = figure.data[0].y[0]
            self.assertTrue(value is None or (isinstance(value, float) and value != value))
            self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
