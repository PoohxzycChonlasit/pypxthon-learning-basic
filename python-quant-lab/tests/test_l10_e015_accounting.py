import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "solutions" / "assessment" / "L10-E015-B.py"
SPEC = importlib.util.spec_from_file_location("l10_e015_b", SOLUTION)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class L10E015AccountingTests(unittest.TestCase):
    valid_account = {"cash": 100, "position": 3}
    rejected_events = (
        ("invalid quantity string", {"quantity": "bad"}, 100, 3),
        ("invalid price string", {"price": "bad"}, 100, 3),
        ("None quantity", {"quantity": None}, 100, 3),
        ("None price", {"price": None}, 100, 3),
        ("empty quantity", {"quantity": ""}, 100, 3),
        ("zero quantity", {"quantity": 0}, 100, 3),
        ("negative quantity", {"quantity": -1}, 100, 3),
        ("zero price", {"price": 0}, 100, 3),
        ("negative price", {"price": -1}, 100, 3),
        ("insufficient position", {"position": 0.5, "quantity": 1}, 100, 0.5),
        ("unsupported side", {"side": "buy"}, 100, 3),
        ("NaN quantity", {"quantity": float("nan")}, 100, 3),
        ("infinite quantity", {"quantity": float("inf")}, 100, 3),
        ("NaN price", {"price": float("nan")}, 100, 3),
        ("infinite price", {"price": float("inf")}, 100, 3),
    )

    def test_rejected_sell_events_preserve_valid_account_balances(self):
        for label, changes, expected_cash, expected_position in self.rejected_events:
            with self.subTest(case=label):
                event = {
                    **self.valid_account,
                    "quantity": 1,
                    "price": 20,
                    "side": "sell",
                    **changes,
                }
                expected = {
                    "accepted": False,
                    "cash_after": expected_cash,
                    "position_after": expected_position,
                    "live_trading": False,
                }
                self.assertEqual(
                    MODULE.final_offline_bot_assessment(event), expected
                )

    def test_valid_sell_updates_cash_and_position(self):
        self.assertEqual(
            MODULE.final_offline_bot_assessment(
                {"cash": 100, "position": 3, "quantity": 1, "price": 20, "side": "sell"}
            ),
            {
                "accepted": True,
                "cash_after": 120,
                "position_after": 2,
                "live_trading": False,
            },
        )

    def test_non_dict_event_keeps_documented_zero_balances(self):
        self.assertEqual(
            MODULE.final_offline_bot_assessment(None),
            {
                "accepted": False,
                "cash_after": 0,
                "position_after": 0,
                "live_trading": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
