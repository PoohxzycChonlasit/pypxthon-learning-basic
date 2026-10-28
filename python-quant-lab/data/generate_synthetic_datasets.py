"""Generate deterministic offline practice datasets; no network access is used."""

from __future__ import annotations

import csv
import random
from datetime import date, datetime, time, timedelta
from pathlib import Path


def write_csv(directory: Path, filename: str, fieldnames: list[str], rows: list[dict]) -> None:
    path = directory / filename
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def make_transactions(seed: int, count: int = 1200) -> list[dict]:
    rng = random.Random(seed)
    products = [
        ("P-100", "books", 8.0, 45.0),
        ("P-200", "home", 12.0, 120.0),
        ("P-300", "office", 2.0, 32.0),
        ("P-400", "sports", 10.0, 180.0),
        ("P-500", "food", 1.0, 24.0),
    ]
    segments = ["new", "returning", "business"]
    start = date(2025, 1, 1)
    rows = []
    for number in range(1, count + 1):
        product, category, low, high = rng.choice(products)
        rows.append(
            {
                "transaction_id": f"TX-{number:05d}",
                "order_date": (start + timedelta(days=rng.randrange(365))).isoformat(),
                "product_id": product,
                "category": category,
                "quantity": rng.randint(1, 8),
                "unit_price": f"{rng.uniform(low, high):.2f}",
                "discount_rate": f"{rng.choice([0, 0, 0, 0.05, 0.10, 0.20]):.2f}",
                "customer_segment": rng.choice(segments),
            }
        )
    rows.sort(key=lambda row: (row["order_date"], row["transaction_id"]))
    # A rare but valid high-value order is useful when inspecting distributions.
    rows[-1]["quantity"] = 40
    return rows


def make_ohlcv(seed: int, symbol: str, starting_price: float, days: int = 730) -> list[dict]:
    rng = random.Random(seed)
    start = date(2024, 1, 1)
    price = starting_price
    rows = []
    # Gaps in dates are intentional; timestamps remain unique and ordered.
    missing_days = {91, 256, 513}
    for index in range(days):
        if index in missing_days:
            continue
        opened = price
        change = rng.normalvariate(0.0002, 0.022)
        closed = max(0.01, opened * (1 + change))
        high = max(opened, closed) * (1 + rng.uniform(0, 0.012))
        low = min(opened, closed) * (1 - rng.uniform(0, 0.012))
        rows.append(
            {
                "timestamp": datetime.combine(start + timedelta(days=index), time()).isoformat() + "Z",
                "symbol": symbol,
                "open": f"{opened:.4f}",
                "high": f"{high:.4f}",
                "low": f"{low:.4f}",
                "close": f"{closed:.4f}",
                "volume": f"{rng.uniform(100, 25000):.4f}",
            }
        )
        price = closed
    return rows


def generate(output_dir: Path | str | None = None) -> Path:
    directory = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent
    directory.mkdir(parents=True, exist_ok=True)

    transaction_fields = [
        "transaction_id", "order_date", "product_id", "category", "quantity",
        "unit_price", "discount_rate", "customer_segment",
    ]
    transactions = make_transactions(20261028)
    write_csv(directory, "ecommerce_transactions.csv", transaction_fields, transactions)

    # Keep dirty training records separate from clean transactions and OHLCV data.
    dirty = [dict(row) for row in transactions[:60]]
    dirty.append(dict(dirty[3]))  # duplicate record
    bad_date = dict(dirty[4]); bad_date.update(transaction_id="DIRTY-DATE", order_date="not-a-date")
    missing = dict(dirty[5]); missing.update(transaction_id="DIRTY-MISSING", unit_price="")
    invalid_number = dict(dirty[6]); invalid_number.update(transaction_id="DIRTY-NUMBER", quantity="many")
    negative = dict(dirty[7]); negative.update(transaction_id="DIRTY-NEGATIVE", quantity=-2)
    invalid_discount = dict(dirty[8]); invalid_discount.update(transaction_id="DIRTY-DISCOUNT", discount_rate="1.5")
    dirty.extend([bad_date, missing, invalid_number, negative, invalid_discount])
    write_csv(directory, "ecommerce_transactions_dirty.csv", transaction_fields, dirty)

    rng = random.Random(7301)
    segment_rows = []
    for i in range(1, 401):
        orders = rng.randint(1, 40)
        segment_rows.append(
            {
                "customer_id": f"C-{i:04d}",
                "segment": rng.choice(["new", "returning", "business", "vip"]),
                "region": rng.choice(["north", "central", "south", "east"]),
                "first_order_date": (date(2023, 1, 1) + timedelta(days=rng.randrange(900))).isoformat(),
                "orders": orders,
                "lifetime_value": f"{rng.uniform(20, 1200):.2f}",
            }
        )
    segment_rows[-1]["lifetime_value"] = "25000.00"  # unusual, valid observation
    write_csv(directory, "customer_segments.csv", list(segment_rows[0]), segment_rows)

    rng = random.Random(4802)
    inventory_rows = []
    start_dt = date(2025, 1, 1)
    for i in range(1, 801):
        inventory_rows.append(
            {
                "movement_id": f"MV-{i:05d}",
                "movement_date": (start_dt + timedelta(days=rng.randrange(365))).isoformat(),
                "sku": rng.choice(["SKU-A", "SKU-B", "SKU-C", "SKU-D", "SKU-E"]),
                "movement_type": (kind := rng.choice(["sale", "restock", "adjustment"])),
                "quantity_delta": -rng.randint(1, 15) if kind == "sale" else rng.randint(1, 30),
                "unit_cost": f"{rng.uniform(1.5, 80):.2f}",
            }
        )
    inventory_rows.sort(key=lambda row: (row["movement_date"], row["movement_id"]))
    write_csv(directory, "inventory_movements.csv", list(inventory_rows[0]), inventory_rows)

    rng = random.Random(9917)
    employee_rows = []
    for i in range(1, 261):
        employee_rows.append(
            {
                "record_id": f"HR-{i:04d}",
                "employee_id": f"EMP-{rng.randint(1, 45):03d}",
                "work_date": (date(2025, 1, 1) + timedelta(days=rng.randrange(180))).isoformat(),
                "hours": f"{rng.choice([4, 6, 7.5, 8, 9, 10]):.1f}",
                "hourly_rate": f"{rng.choice([180, 220, 260, 320]):.2f}",
            }
        )
    employee_rows.sort(key=lambda row: (row["work_date"], row["record_id"]))
    write_csv(directory, "employee_time_records.csv", list(employee_rows[0]), employee_rows)

    rng = random.Random(1182)
    channels = ["search", "social", "email", "referral", "direct"]
    sessions = []
    for day_index in range(365):
        current = date(2025, 1, 1) + timedelta(days=day_index)
        for channel in channels:
            count = rng.randint(40, 900)
            conversions = rng.randint(0, max(1, count // 8))
            sessions.append(
                {"date": current.isoformat(), "channel": channel, "sessions": count, "conversions": conversions}
            )
    sessions[300]["sessions"] = 50000  # unusual, valid traffic spike for anomaly review
    write_csv(directory, "website_sessions.csv", list(sessions[0]), sessions)

    rng = random.Random(4205)
    expenses = []
    for month_index in range(60):
        year = 2021 + month_index // 12
        month = month_index % 12 + 1
        for department in ["sales", "operations", "engineering", "support"]:
            expenses.append(
                {
                    "month": f"{year:04d}-{month:02d}",
                    "department": department,
                    "category": rng.choice(["travel", "software", "supplies", "services"]),
                    "amount": f"{rng.uniform(50, 9000):.2f}",
                }
            )
    write_csv(directory, "monthly_business_expenses.csv", list(expenses[0]), expenses)

    btc = make_ohlcv(8107, "SYNTH-BTC", 42000.0)
    eth = make_ohlcv(8108, "SYNTH-ETH", 2200.0)
    ohlcv_fields = ["timestamp", "symbol", "open", "high", "low", "close", "volume"]
    write_csv(directory, "synthetic_btc_ohlcv_daily.csv", ohlcv_fields, btc)
    write_csv(directory, "synthetic_eth_ohlcv_daily.csv", ohlcv_fields, eth)

    rng = random.Random(2099)
    trades = []
    for i in range(1, 501):
        entry_day = date(2025, 1, 1) + timedelta(days=i // 2)
        entry = rng.uniform(15, 150)
        exit_price = entry * (1 + rng.normalvariate(0, 0.04))
        trades.append(
            {
                "trade_id": f"PAPER-{i:05d}",
                "entry_time": datetime.combine(entry_day, time(9)).isoformat() + "Z",
                "exit_time": datetime.combine(entry_day, time(16)).isoformat() + "Z",
                "symbol": rng.choice(["SYNTH-A", "SYNTH-B", "SYNTH-C"]),
                "side": rng.choice(["long", "short"]),
                "entry_price": f"{entry:.4f}",
                "exit_price": f"{exit_price:.4f}",
                "quantity": f"{rng.uniform(0.1, 8):.4f}",
                "fee_rate": "0.0010",
            }
        )
    write_csv(directory, "synthetic_paper_trades.csv", list(trades[0]), trades)
    return directory


if __name__ == "__main__":
    print(f"Generated deterministic synthetic datasets in {generate()}")
