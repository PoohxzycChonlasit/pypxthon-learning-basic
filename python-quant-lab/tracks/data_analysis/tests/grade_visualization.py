"""Run after approval installs Matplotlib and the student completes DA18–DA19."""

import sys
import tempfile
import unittest
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

EXERCISES = Path(__file__).resolve().parents[1] / "exercises"
sys.path.insert(0, str(EXERCISES))
from visualization import business_charts, ohlcv_chart


class VisualizationSubmissionTests(unittest.TestCase):
    def test_DA18_chart_types_labels_and_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sessions.csv"
            path.write_text(
                "date,channel,sessions,conversions\n"
                "2025-01-01,email,10,1\n2025-01-01,search,30,3\n2025-01-02,email,20,2\n",
                encoding="utf-8",
            )
            figure = business_charts(path)
            self.assertEqual(len(figure.axes), 4)
            self.assertEqual([axis.get_ylabel() for axis in figure.axes], ["Sessions", "Sessions", "Count", "Conversions"])
            self.assertEqual(figure.axes[0].lines[0].get_ydata().tolist(), [40, 20])
            self.assertEqual(figure.axes[3].collections[0].get_offsets().tolist(), [[10, 1], [30, 3], [20, 2]])
            plt.close(figure)

    def test_DA19_ohlcv_validation_and_saved_chart_artifact(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "synthetic.csv"
            source.write_text(
                "timestamp,open,high,low,close,volume\n"
                "2025-01-01,10,12,9,11,100\n2025-01-02,11,13,10,12,120\n",
                encoding="utf-8",
            )
            output = folder / "ohlcv.png"
            figure = ohlcv_chart(source, output)
            self.assertTrue(output.is_file())
            self.assertGreater(output.stat().st_size, 500)
            self.assertEqual(figure.axes[0].get_ylabel(), "Synthetic price")
            self.assertEqual(figure.axes[1].get_ylabel(), "Volume")
            self.assertEqual(figure.axes[0].lines[0].get_ydata().tolist(), [11.0, 12.0])
            plt.close(figure)

    def test_DA19_rejects_invalid_ohlcv_rows(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            source = folder / "invalid.csv"
            output = folder / "invalid.png"
            cases = [
                "timestamp,open,high,low,close,volume\n2025-01-01,10,9,8,9,10\n",
                "timestamp,open,high,low,close,volume\n2025-01-01,10,12,8,11,-1\n",
                "timestamp,open,high,low,close,volume\n2025-01-01,10,12,8,nan,10\n",
                "timestamp,open,high,low,close,volume\n2025-01-02,10,12,8,11,10\n2025-01-01,10,12,8,11,10\n",
            ]
            for content in cases:
                source.write_text(content, encoding="utf-8")
                with self.assertRaises(ValueError):
                    ohlcv_chart(source, output)


if __name__ == "__main__":
    unittest.main()
