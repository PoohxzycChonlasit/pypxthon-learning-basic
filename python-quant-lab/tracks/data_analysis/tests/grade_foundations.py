"""Run this grader after implementing DA01–DA05 in exercises/foundations.py."""

import csv
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "exercises"))
from foundations import clean_transaction_rows, dataset_profile, load_csv_records, load_json_records, monthly_revenue


class FoundationSubmissionTests(unittest.TestCase):
    def test_DA01_profile(self):
        self.assertEqual(dataset_profile([{"sku": "A", "qty": 2}, {"sku": "B", "qty": ""}, {"sku": "A", "qty": 2}]),
                         {"rows": 3, "columns": ["sku", "qty"], "missing_cells": 1, "duplicate_rows": 1})

    def test_DA01_missing_schema_cell_counts_as_missing(self):
        self.assertEqual(dataset_profile([{"sku": "A", "qty": 2}, {"sku": "B"}, {"sku": "C", "qty": ""}]),
                         {"rows": 3, "columns": ["sku", "qty"], "missing_cells": 2, "duplicate_rows": 0})

    def test_DA02_csv(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sales.csv"
            path.write_text('sku,qty\n"A, special",2\n', encoding="utf-8")
            self.assertEqual(load_csv_records(path), [{"sku": "A, special", "qty": "2"}])

    def test_DA02_rejects_empty_or_blank_headers(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "bad.csv"
            for content in ("", "\n", ",qty\n"):
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_csv_records(path)

    def test_DA03_json(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "config.json"
            path.write_text('{"records": [{"id": 1}]}', encoding="utf-8")
            self.assertEqual(load_json_records(path), [{"id": 1}])

    def test_DA03_accepts_list_and_rejects_invalid_shapes(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "records.json"
            path.write_text('[{"id": 1}]', encoding="utf-8")
            self.assertEqual(load_json_records(path), [{"id": 1}])
            for content in ('{"records": 2}', '[1]', 'null'):
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_json_records(path)

    def test_DA04_sqlite(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sales.db"
            connection = sqlite3.connect(path)
            try:
                connection.execute("CREATE TABLE sales(order_date TEXT, quantity INTEGER, unit_price REAL)")
                connection.executemany("INSERT INTO sales VALUES (?, ?, ?)", [("2025-02-01", 3, 4), ("2025-01-01", 2, 5)])
                connection.commit()
            finally:
                connection.close()
            self.assertEqual(monthly_revenue(path), [("2025-01", 10.0), ("2025-02", 12.0)])

    def test_DA05_dirty_rows(self):
        with (ROOT / "data" / "ecommerce_transactions_dirty.csv").open(encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))
        original = [dict(row) for row in rows]
        result = clean_transaction_rows(rows)
        self.assertEqual((len(result["accepted"]), len(result["rejected"])), (60, 6))
        self.assertEqual(rows, original)
        self.assertIn("duplicate transaction_id", {row["reason"] for row in result["rejected"]})

    def test_DA05_nonfinite_price_is_rejected_without_mutation(self):
        rows = [{"transaction_id": "T1", "order_date": "2025-01-01", "quantity": "1",
                 "unit_price": "inf", "discount_rate": "0"}]
        original = [dict(row) for row in rows]
        result = clean_transaction_rows(rows)
        self.assertEqual(len(result["accepted"]), 0)
        self.assertEqual(result["rejected"][0]["reason"], "unit_price must be finite and nonnegative")
        self.assertEqual(rows, original)



if __name__ == "__main__":
    unittest.main()
