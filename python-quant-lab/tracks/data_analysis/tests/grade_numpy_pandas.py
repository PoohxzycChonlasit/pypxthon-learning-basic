"""Run after approval installs NumPy and pandas and the student fills DA06–DA17/22."""

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd


EXERCISES = Path(__file__).resolve().parents[1] / "exercises"
sys.path.insert(0, str(EXERCISES))
from numpy_practice import apply_column_weights, make_price_array, numeric_summary, select_close_window
from pandas_practice import (
    clean_event_csv,
    csv_overview,
    daily_price_features,
    eda_summary,
    export_analysis,
    filter_sort_sales,
    sales_by_category,
    series_profile,
    time_based_split,
)


def write_csv(path, header, rows):
    path.write_text(header + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


class NumpySubmissionTests(unittest.TestCase):
    def test_DA06_create_float_array(self):
        source = [10, 20.5]
        result = make_price_array(source)
        self.assertEqual(result.shape, (2,))
        self.assertTrue(np.issubdtype(result.dtype, np.floating))
        np.testing.assert_allclose(result, [10.0, 20.5])
        self.assertEqual(source, [10, 20.5])
        self.assertEqual(make_price_array([]).shape, (0,))

    def test_DA07_index_and_slice_close_column(self):
        matrix = [[1, 1.3, 0.8, 1.2], [2, 2.4, 1.7, 2.2], [3, 3.5, 2.8, 3.1]]
        np.testing.assert_allclose(select_close_window(matrix, 1, 3), [2.2, 3.1])
        np.testing.assert_allclose(select_close_window(matrix, 2, 2), [])

    def test_DA08_vectorize_with_column_broadcasting(self):
        matrix = np.array([[1, 2], [3, 4]], dtype=float)
        actual = apply_column_weights(matrix, [10, 0.5])
        np.testing.assert_allclose(actual, [[10, 1], [30, 2]])
        np.testing.assert_allclose(matrix, [[1, 2], [3, 4]])

    def test_DA09_population_summary(self):
        result = numeric_summary([2, 4, 6])
        self.assertEqual(result["sum"], 12.0)
        self.assertEqual(result["mean"], 4.0)
        self.assertAlmostEqual(result["std"], np.sqrt(8 / 3))
        self.assertEqual((result["min"], result["max"]), (2.0, 6.0))

    def test_DA06_rejects_multidimensional_input(self):
        with self.assertRaises(ValueError):
            make_price_array([[1, 2], [3, 4]])

    def test_DA07_slice_is_independent_and_validates_shape(self):
        matrix = [[1, 2, 0, 1.5], [2, 3, 1, 2.5]]
        result = select_close_window(matrix, 0, 1)
        result[0] = -99
        self.assertEqual(matrix[0][3], 1.5)
        with self.assertRaises(ValueError):
            select_close_window([[1, 2, 3]], 0, 1)

    def test_DA08_rejects_weight_shape_mismatch(self):
        with self.assertRaises(ValueError):
            apply_column_weights([[1, 2]], [3])

    def test_DA09_rejects_empty_nonfinite_and_multidimensional_data(self):
        for values in ([], [1, float("nan")], [[1, 2]]):
            with self.assertRaises(ValueError):
                numeric_summary(values)



class PandasSubmissionTests(unittest.TestCase):
    def test_DA10_series_missing_profile_keeps_zero(self):
        self.assertEqual(series_profile([2, None, 0, 4, np.nan]),
                         {"count": 3, "missing": 2, "mean": 2.0, "median": 2.0})
        self.assertEqual(series_profile([None])["mean"], None)

    def test_DA11_read_csv_head_info_and_describe(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sales.csv"
            write_csv(path, "order_id,category,quantity,unit_price", ["A,books,2,5", "B,home,1,8", "C,books,3,4"])
            result = csv_overview(path)
            self.assertEqual(result["shape"], (3, 4))
            self.assertEqual(result["columns"], ["order_id", "category", "quantity", "unit_price"])
            self.assertEqual(len(result["head"]), 3)
            self.assertIn("quantity", result["info"])
            self.assertEqual(result["describe"]["quantity"]["count"], 3.0)

    def test_DA12_loc_filter_iloc_columns_and_sort_order(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sales.csv"
            write_csv(path, "order_id,product,category,quantity,unit_price",
                      ["A,book,books,2,5", "B,pen,books,3,4", "C,mug,home,1,9"])
            self.assertEqual(filter_sort_sales(path, "books", 10), [
                {"order_id": "B", "product": "pen", "revenue": 12},
                {"order_id": "A", "product": "book", "revenue": 10},
            ])

    def test_DA13_invalid_and_duplicate_events_are_quarantined(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "events.csv"
            write_csv(path, "event_id,timestamp,value", [
                "A,2025-01-01,2", "A,2025-01-02,4", "B,not-a-date,5", "C,2025-01-03,bad", "D,2025-01-04,-1", "E,2025-01-05,inf"
            ])
            result = clean_event_csv(path)
            self.assertEqual(len(result["accepted"]), 1)
            self.assertEqual(len(result["rejected"]), 5)
            self.assertEqual({item["reason"] for item in result["rejected"]}, {
                "duplicate event_id", "invalid timestamp", "invalid value", "value must be nonnegative", "value must be finite"
            })

    def test_DA14_groupby_aggregation_and_many_to_one_merge(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            transactions = folder / "transactions.csv"
            products = folder / "products.csv"
            write_csv(transactions, "transaction_id,product_id,quantity,unit_price",
                      ["T1,P1,2,5", "T2,P1,1,5", "T3,P2,1,8"])
            write_csv(products, "product_id,category", ["P1,books", "P2,home"])
            self.assertEqual(sales_by_category(transactions, products), [
                {"category": "books", "order_count": 2, "revenue": 15},
                {"category": "home", "order_count": 1, "revenue": 8},
            ])

    def test_DA14_rejects_unmatched_and_duplicate_product_keys(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            transactions = folder / "transactions.csv"
            products = folder / "products.csv"
            write_csv(transactions, "transaction_id,product_id,quantity,unit_price", ["T1,P1,1,5"])
            write_csv(products, "product_id,category", ["P2,home"])
            with self.assertRaises(ValueError):
                sales_by_category(transactions, products)
            write_csv(products, "product_id,category", ["P1,books", "P1,home"])
            with self.assertRaises(pd.errors.MergeError):
                sales_by_category(transactions, products)

    def test_DA15_resample_rolling_lag_and_change_preserve_gap(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "prices.csv"
            write_csv(path, "timestamp,close", [
                "2025-01-01,100", "2025-01-02,110", "2025-01-04,121"
            ])
            result = daily_price_features(path, window=2)
            self.assertEqual(len(result), 4)
            self.assertTrue(pd.isna(result.loc["2025-01-03", "close"]))
            self.assertAlmostEqual(result.loc["2025-01-02", "rolling_mean"], 105.0)
            self.assertTrue(pd.isna(result.loc["2025-01-04", "pct_change"]))
            self.assertTrue(pd.isna(result.loc["2025-01-04", "rolling_mean"]))

    def test_DA16_time_split_never_shuffles_across_cut(self):
        frame = pd.DataFrame({"timestamp": ["2025-01-04", "2025-01-01", "2025-01-03"], "value": [4, 1, 3]})
        train, test = time_based_split(frame, "timestamp", "2025-01-03")
        self.assertEqual(train["value"].tolist(), [1])
        self.assertEqual(test["value"].tolist(), [3, 4])
        self.assertLess(train["timestamp"].max(), test["timestamp"].min())

    def test_DA16_split_returns_independent_frames_and_preserves_input(self):
        frame = pd.DataFrame({"timestamp": ["2025-01-02", "2025-01-01"], "value": [2, 1]})
        original = frame.copy(deep=True)
        train, test = time_based_split(frame, "timestamp", "2025-01-02")
        train.loc[train.index[0], "value"] = 999
        pd.testing.assert_frame_equal(frame, original)
        self.assertEqual(test["value"].tolist(), [2])

    def test_DA17_eda_summary_reports_statistics_quality_and_relationships(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sessions.csv"
            write_csv(path, "date,channel,sessions,conversions", [
                "2025-01-01,A,10,1", "2025-01-02,A,20,2", "2025-02-01,B,30,5", "2025-02-02,B,1000,50"
            ])
            result = eda_summary(path, "sessions", "conversions", "channel", "date")
            self.assertEqual((result["rows"], result["missing_cells"], result["duplicate_rows"]), (4, 0, 0))
            self.assertEqual(result["description"]["mean"], 265.0)
            self.assertEqual(result["outlier_count_iqr"], 1)
            self.assertEqual(result["monthly_trend"], {"2025-01": 30.0, "2025-02": 1030.0})
            self.assertGreater(result["correlation"], 0.99)
            self.assertEqual(sum(result["distribution_counts"]), 4)

    def test_DA17_reports_missing_cells_and_duplicate_rows(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "quality.csv"
            write_csv(path, "date,channel,sessions,conversions", [
                "2025-01-01,A,10,1", "2025-01-02,A,20,2", "2025-01-02,A,20,2", "2025-02-01,B,,5"
            ])
            result = eda_summary(path, "sessions", "conversions", "channel", "date")
            self.assertEqual((result["rows"], result["missing_cells"], result["duplicate_rows"]), (4, 1, 1))

    def test_DA22_export_has_no_index_column_and_round_trips(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "report.csv"
            frame = pd.DataFrame({"channel": ["email", "search"], "sessions": [10, 20]})
            result = export_analysis(frame, path)
            self.assertEqual(result["rows"], 2)
            loaded = pd.read_csv(path)
            self.assertEqual(list(loaded.columns), ["channel", "sessions"])
            pd.testing.assert_frame_equal(loaded, frame)


if __name__ == "__main__":
    unittest.main()
