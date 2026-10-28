"""Run after approval installs NumPy/pandas and the student completes DA20–DA21."""

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np


EXERCISES = Path(__file__).resolve().parents[1] / "exercises"
sys.path.insert(0, str(EXERCISES))
from capstone import business_kpis, financial_metrics


class CapstoneSubmissionTests(unittest.TestCase):
    def test_DA20_business_kpis_are_reconciled(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            transactions = folder / "transactions.csv"
            sessions = folder / "sessions.csv"
            inventory = folder / "inventory.csv"
            transactions.write_text(
                "transaction_id,quantity,unit_price,discount_rate,customer_segment\n"
                "T1,2,10,0.1,new\nT2,1,20,0,returning\n",
                encoding="utf-8",
            )
            sessions.write_text("date,channel,sessions,conversions\n2025-01-01,email,100,10\n", encoding="utf-8")
            inventory.write_text(
                "movement_id,movement_date,sku,quantity_delta,unit_cost\n"
                "M1,2025-01-01,A,-5,2\nM2,2025-01-02,A,2,2\nM3,2025-01-02,B,3,4\n",
                encoding="utf-8",
            )
            result = business_kpis(transactions, sessions, inventory)
            self.assertEqual(result["order_count"], 2)
            self.assertEqual(result["total_revenue"], 38.0)
            self.assertEqual(result["average_order_value"], 19.0)
            self.assertAlmostEqual(result["conversion_rate"], 0.1)
            self.assertEqual(result["revenue_by_segment"], {"new": 18.0, "returning": 20.0})
            self.assertEqual(result["net_inventory_movement_by_sku"], {"A": -3, "B": 3})

    def test_DA20_zero_sessions_has_no_division_by_zero(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            transactions = folder / "transactions.csv"
            sessions = folder / "sessions.csv"
            inventory = folder / "inventory.csv"
            transactions.write_text("transaction_id,quantity,unit_price,discount_rate,customer_segment\n", encoding="utf-8")
            sessions.write_text("date,channel,sessions,conversions\n2025-01-01,email,0,0\n", encoding="utf-8")
            inventory.write_text("movement_id,movement_date,sku,quantity_delta,unit_cost\n", encoding="utf-8")
            self.assertIsNone(business_kpis(transactions, sessions, inventory)["conversion_rate"])

    def test_DA21_returns_costs_equity_and_drawdown(self):
        result = financial_metrics([100, 110, 100], [1, 1], 0.01)
        np.testing.assert_allclose(result["simple_returns"], [0.1, -1 / 11])
        np.testing.assert_allclose(result["log_returns"], [np.log(1.1), np.log(10 / 11)])
        np.testing.assert_allclose(result["net_returns"], [0.09, -1 / 11 - 0.01])
        self.assertEqual(len(result["equity_curve"]), 2)
        self.assertLess(result["max_drawdown"], 0)
        self.assertLessEqual(max(result["drawdowns"]), 0)

    def test_DA21_rejects_invalid_price_or_signal_alignment(self):
        with self.assertRaises(ValueError):
            financial_metrics([100, 0], [1], 0.01)
        with self.assertRaises(ValueError):
            financial_metrics([100, 110], [], 0.01)

    def test_DA21_rejects_costs_that_create_total_loss_or_worse(self):
        with self.assertRaises(ValueError):
            financial_metrics([100, 110], [-1], 0.99)
        with self.assertRaises(ValueError):
            financial_metrics([100, 110], [1], float("nan"))



if __name__ == "__main__":
    unittest.main()
