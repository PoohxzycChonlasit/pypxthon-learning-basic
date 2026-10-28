"""Reference implementations for the standard-library foundations track."""

import csv
import json
import math
import sqlite3
from datetime import date
from pathlib import Path


def dataset_profile(rows):
    columns = list(rows[0].keys()) if rows else []
    missing = sum(row.get(column) is None or row.get(column) == "" for row in rows for column in columns)
    seen = set()
    duplicates = 0
    for row in rows:
        marker = tuple(sorted(row.items()))
        if marker in seen:
            duplicates += 1
        seen.add(marker)
    return {"rows": len(rows), "columns": columns, "missing_cells": missing, "duplicate_rows": duplicates}


def load_csv_records(path):
    with Path(path).open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if (not reader.fieldnames or any(not name.strip() for name in reader.fieldnames)
                or len(set(reader.fieldnames)) != len(reader.fieldnames)):
            raise ValueError("CSV header must contain unique, nonblank names")
        return list(reader)


def load_json_records(path):
    with Path(path).open(encoding="utf-8") as file:
        value = json.load(file)
    records = value.get("records") if isinstance(value, dict) else value
    if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
        raise ValueError("JSON must contain a list of record objects")
    return records


def monthly_revenue(database_path):
    query = """
        SELECT substr(order_date, 1, 7) AS month,
               ROUND(SUM(quantity * unit_price), 2) AS revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    """
    connection = sqlite3.connect(database_path)
    try:
        return [(month, float(revenue)) for month, revenue in connection.execute(query)]
    finally:
        connection.close()


def clean_transaction_rows(rows):
    accepted = []
    rejected = []
    seen = set()
    for row in rows:
        record_id = row.get("transaction_id", "")
        reason = None
        if not record_id:
            reason = "missing transaction_id"
        elif record_id in seen:
            reason = "duplicate transaction_id"
        else:
            seen.add(record_id)
            try:
                date.fromisoformat(str(row.get("order_date", "")))
            except ValueError:
                reason = "invalid order_date"
            if reason is None:
                try:
                    quantity = int(row.get("quantity", ""))
                    unit_price = float(row.get("unit_price", ""))
                    discount_rate = float(row.get("discount_rate", ""))
                except (TypeError, ValueError):
                    reason = "invalid numeric field"
            if reason is None and quantity <= 0:
                reason = "quantity must be positive"
            if reason is None and (not math.isfinite(unit_price) or unit_price < 0):
                reason = "unit_price must be finite and nonnegative"
            if reason is None and (not math.isfinite(discount_rate) or not 0 <= discount_rate <= 1):
                reason = "discount_rate must be between 0 and 1"
        if reason:
            rejected.append({"id": record_id or None, "reason": reason})
        else:
            normalized = dict(row)
            normalized.update(quantity=quantity, unit_price=unit_price, discount_rate=discount_rate)
            accepted.append(normalized)
    return {"accepted": accepted, "rejected": rejected}
