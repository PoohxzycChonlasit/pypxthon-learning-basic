import tempfile
import unittest
from pathlib import Path

from reference import DEFAULT_DATA, load_bars, run_paper_bot, signal_for


class OfflinePaperBotTests(unittest.TestCase):
    def test_synthetic_data_obeys_ohlcv_invariants(self):
        bars = load_bars(DEFAULT_DATA)
        self.assertGreater(len(bars), 0)
        for bar in bars:
            self.assertGreaterEqual(bar["high"], max(bar["open"], bar["close"]))
            self.assertLessEqual(bar["low"], min(bar["open"], bar["close"]))
            self.assertGreaterEqual(bar["volume"], 0)

    def test_unsorted_timestamp_is_rejected(self):
        csv_text = (
            "timestamp,open,high,low,close,volume\n"
            "2026-01-02T00:00:00Z,10,11,9,10,1\n"
            "2026-01-01T00:00:00Z,10,11,9,10,1\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bars.csv"
            source.write_text(csv_text, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "timestamp"):
                load_bars(source)

    def test_future_values_do_not_change_past_signal(self):
        prefix = [100, 102, 101]
        with_future = [100, 102, 101, 5000, 1]
        self.assertEqual(signal_for(prefix, 2), signal_for(with_future, 2))

    def test_fee_reduces_result_and_replay_is_deterministic(self):
        bars = load_bars(DEFAULT_DATA)
        with_fee = run_paper_bot(bars, fee_rate=0.001)
        no_fee = run_paper_bot(bars, fee_rate=0.0)
        self.assertLess(with_fee["net_pnl"], no_fee["net_pnl"])
        self.assertEqual(with_fee, run_paper_bot(bars, fee_rate=0.001))
        self.assertFalse(with_fee["live_trading"])

    def test_order_limits_and_cash_accounting(self):
        report = run_paper_bot(load_bars(DEFAULT_DATA))
        self.assertGreaterEqual(report["final_cash"], 0)
        for event in report["events"]:
            self.assertLessEqual(event["quantity"] * event["price"], 25.0 + 1e-9)
            self.assertGreaterEqual(event["quantity"], 0)
        self.assertEqual(report["final_cash"], report["initial_cash"] + report["net_pnl"])

    def test_empty_bars_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "อย่างน้อยหนึ่งแท่ง"):
            run_paper_bot([])


if __name__ == "__main__":
    unittest.main()
