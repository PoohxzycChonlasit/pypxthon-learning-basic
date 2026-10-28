"""Deterministic synthetic-data and market-fixture quality checks."""

import csv
import runpy
import tempfile
import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = runpy.run_path(str(ROOT / "data" / "generate_synthetic_datasets.py"))


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


class SyntheticDatasetQuality(unittest.TestCase):
    def test_expected_dataset_sizes_and_clean_transaction_schema(self):
        expected = {
            "ecommerce_transactions.csv": 1200,
            "customer_segments.csv": 400,
            "inventory_movements.csv": 800,
            "employee_time_records.csv": 260,
            "website_sessions.csv": 1825,
            "monthly_business_expenses.csv": 240,
            "synthetic_btc_ohlcv_daily.csv": 727,
            "synthetic_eth_ohlcv_daily.csv": 727,
            "synthetic_paper_trades.csv": 500,
        }
        for filename, count in expected.items():
            with self.subTest(filename=filename):
                rows = read_rows(ROOT / "data" / filename)
                self.assertEqual(len(rows), count)
                self.assertTrue(rows)

        transactions = read_rows(ROOT / "data" / "ecommerce_transactions.csv")
        self.assertEqual(len({row["transaction_id"] for row in transactions}), 1200)
        self.assertEqual(set(transactions[0]), {
            "transaction_id", "order_date", "product_id", "category", "quantity",
            "unit_price", "discount_rate", "customer_segment",
        })
        self.assertTrue(all(int(row["quantity"]) > 0 for row in transactions))
        self.assertTrue(all(float(row["unit_price"]) > 0 for row in transactions))

    def test_dirty_transactions_expose_documented_quality_problems(self):
        rows = read_rows(ROOT / "data" / "ecommerce_transactions_dirty.csv")
        self.assertEqual(len(rows), 66)
        identifiers = [row["transaction_id"] for row in rows]
        self.assertLess(len(set(identifiers)), len(identifiers))
        self.assertIn("", [row["unit_price"] for row in rows])
        self.assertIn("many", [row["quantity"] for row in rows])
        self.assertIn("-2", [row["quantity"] for row in rows])
        self.assertIn("1.5", [row["discount_rate"] for row in rows])
        self.assertIn("not-a-date", [row["order_date"] for row in rows])

    def test_ohlcv_market_fixtures_are_valid_and_ordered(self):
        for filename in ("synthetic_btc_ohlcv_daily.csv", "synthetic_eth_ohlcv_daily.csv"):
            rows = read_rows(ROOT / "data" / filename)
            stamps = [datetime.fromisoformat(row["timestamp"].removesuffix("Z")) for row in rows]
            self.assertEqual(stamps, sorted(stamps), filename)
            self.assertEqual(len(stamps), len(set(stamps)), filename)
            self.assertTrue(any((right - left).days > 1 for left, right in zip(stamps, stamps[1:])))
            for row in rows:
                opened, high, low, close, volume = (
                    float(row[key]) for key in ("open", "high", "low", "close", "volume")
                )
                self.assertGreater(opened, 0)
                self.assertGreater(high, 0)
                self.assertGreater(low, 0)
                self.assertGreater(close, 0)
                self.assertGreaterEqual(volume, 0)
                self.assertGreaterEqual(high, max(opened, close))
                self.assertLessEqual(low, min(opened, close))
                self.assertLessEqual(low, high)

    def test_generator_is_reproducible_in_an_isolated_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first"
            second = Path(temporary) / "second"
            GENERATOR["generate"](first)
            GENERATOR["generate"](second)
            first_files = {path.name: path.read_bytes() for path in first.glob("*.csv")}
            second_files = {path.name: path.read_bytes() for path in second.glob("*.csv")}
            self.assertEqual(first_files, second_files)


if __name__ == "__main__":
    unittest.main()
