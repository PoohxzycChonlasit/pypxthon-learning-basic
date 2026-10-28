"""Verified standard-library answer key and clean/dirty fixture checks."""

import csv
import importlib.util
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SOLUTION_PATH = Path(__file__).resolve().parents[1] / "solutions" / "foundations.py"
spec = importlib.util.spec_from_file_location("foundation_solutions", SOLUTION_PATH)
solutions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solutions)


class FoundationReferenceTests(unittest.TestCase):
    def test_profile_counts_schema_missing_and_duplicate_rows(self):
        rows = [
            {"sku": "A", "qty": 2},
            {"sku": "B", "qty": ""},
            {"sku": "A", "qty": 2},
        ]
        self.assertEqual(solutions.dataset_profile(rows), {
            "rows": 3, "columns": ["sku", "qty"], "missing_cells": 1, "duplicate_rows": 1
        })
        self.assertEqual(solutions.dataset_profile([])["columns"], [])

    def test_csv_and_json_ingestion_and_schema_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            csv_path = folder / "rows.csv"
            csv_path.write_text("sku,qty\nA-1,2\n", encoding="utf-8")
            self.assertEqual(solutions.load_csv_records(csv_path), [{"sku": "A-1", "qty": "2"}])
            (folder / "empty.csv").write_text("", encoding="utf-8")
            with self.assertRaises(ValueError):
                solutions.load_csv_records(folder / "empty.csv")

            list_path = folder / "list.json"
            list_path.write_text('[{"id": 1}]', encoding="utf-8")
            self.assertEqual(solutions.load_json_records(list_path), [{"id": 1}])
            object_path = folder / "object.json"
            object_path.write_text('{"records": [{"id": 2}]}', encoding="utf-8")
            self.assertEqual(solutions.load_json_records(object_path), [{"id": 2}])
            bad_path = folder / "bad.json"
            bad_path.write_text('{"records": [1]}', encoding="utf-8")
            with self.assertRaises(ValueError):
                solutions.load_json_records(bad_path)

    def test_sqlite_monthly_revenue(self):
        with tempfile.TemporaryDirectory() as temporary:
            db = Path(temporary) / "sales.db"
            connection = sqlite3.connect(db)
            try:
                connection.execute("CREATE TABLE sales(order_date TEXT, quantity INTEGER, unit_price REAL)")
                connection.executemany(
                    "INSERT INTO sales VALUES (?, ?, ?)",
                    [("2025-01-01", 2, 5), ("2025-01-22", 1, 6), ("2025-02-01", 3, 4)],
                )
                connection.commit()
            finally:
                connection.close()
            self.assertEqual(solutions.monthly_revenue(db), [("2025-01", 16.0), ("2025-02", 12.0)])

    def test_dirty_transaction_fixture_is_cleaned_without_mutating_input(self):
        with (PROJECT_ROOT / "data" / "ecommerce_transactions_dirty.csv").open(
            encoding="utf-8", newline=""
        ) as file:
            rows = list(csv.DictReader(file))
        original = [dict(row) for row in rows]
        result = solutions.clean_transaction_rows(rows)
        self.assertEqual(len(result["accepted"]), 60)
        self.assertEqual(len(result["rejected"]), 6)
        self.assertEqual(rows, original)
        reasons = {item["reason"] for item in result["rejected"]}
        self.assertEqual(reasons, {
            "duplicate transaction_id", "invalid order_date", "invalid numeric field",
            "quantity must be positive", "discount_rate must be between 0 and 1",
        })


if __name__ == "__main__":
    unittest.main()
