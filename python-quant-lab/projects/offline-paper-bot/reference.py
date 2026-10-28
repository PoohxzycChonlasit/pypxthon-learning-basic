"""Reference implementation for the offline paper-bot capstone."""
from __future__ import annotations

import csv
import logging
import math
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA = PROJECT_ROOT / "data" / "synthetic_btc_ohlcv.csv"
REQUIRED = ("timestamp", "open", "high", "low", "close", "volume")


def load_bars(path: Path = DEFAULT_DATA) -> list[dict]:
    bars = []
    previous_time = None
    with Path(path).open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or not set(REQUIRED).issubset(reader.fieldnames):
            raise ValueError("CSV ต้องมีคอลัมน์ timestamp, open, high, low, close, volume")
        for line_number, row in enumerate(reader, start=2):
            try:
                timestamp = datetime.fromisoformat(row["timestamp"].replace("Z", "+00:00"))
                bar = {key: float(row[key]) for key in ("open", "high", "low", "close", "volume")}
            except (AttributeError, TypeError, ValueError) as error:
                raise ValueError(f"แถว {line_number}: เวลา หรือ OHLCV ไม่ถูกต้อง") from error
            if previous_time is not None and timestamp <= previous_time:
                raise ValueError(f"แถว {line_number}: timestamp ต้องเรียงเพิ่มและห้ามซ้ำ")
            if any(not math.isfinite(value) for value in bar.values()):
                raise ValueError(f"แถว {line_number}: ห้ามใช้ค่า NaN หรือ infinity")
            if min(bar["open"], bar["high"], bar["low"], bar["close"]) <= 0:
                raise ValueError(f"แถว {line_number}: ราคาต้องมากกว่าศูนย์")
            if bar["volume"] < 0:
                raise ValueError(f"แถว {line_number}: volume ห้ามติดลบ")
            if bar["high"] < max(bar["open"], bar["close"]):
                raise ValueError(f"แถว {line_number}: high ต่ำกว่า open หรือ close")
            if bar["low"] > min(bar["open"], bar["close"]) or bar["low"] > bar["high"]:
                raise ValueError(f"แถว {line_number}: low ไม่สอดคล้องกับ OHLC")
            bars.append({"timestamp": timestamp, **bar})
            previous_time = timestamp
    if not bars:
        raise ValueError("ไม่พบแถวข้อมูล OHLCV")
    return bars


def signal_for(closes, index, window=2):
    """Evaluate after bar index closes, using only the preceding window closes."""
    if window < 1 or index < window or index >= len(closes):
        return "hold"
    reference = sum(closes[index - window:index]) / window
    if closes[index] > reference:
        return "buy"
    if closes[index] < reference:
        return "sell"
    return "hold"


def run_paper_bot(
    bars,
    initial_cash=100.0,
    max_order_value=25.0,
    max_units=0.2,
    fee_rate=0.001,
    max_drawdown=10.0,
    window=2,
):
    if not bars:
        raise ValueError("ต้องมีข้อมูลอย่างน้อยหนึ่งแท่ง")
    if initial_cash <= 0 or max_order_value <= 0 or max_units <= 0:
        raise ValueError("เงินเริ่มต้นและ risk limits ต้องมากกว่าศูนย์")
    if fee_rate < 0 or max_drawdown <= 0:
        raise ValueError("fee_rate ห้ามติดลบและ max_drawdown ต้องมากกว่าศูนย์")

    closes = [float(bar["close"]) for bar in bars]
    cash = float(initial_cash)
    units = 0.0
    events = []
    peak_equity = cash
    maximum_drawdown_seen = 0.0
    stopped_for_risk = False
    logger = logging.getLogger("offline_paper_bot")

    def record(action, bar, price, quantity, fee):
        event = {
            "timestamp": bar["timestamp"].isoformat() if isinstance(bar["timestamp"], datetime) else str(bar["timestamp"]),
            "action": action,
            "price": price,
            "quantity": quantity,
            "fee": fee,
            "cash": round(cash, 8),
            "units": round(units, 8),
        }
        events.append(event)
        logger.info("%s", event)

    for index in range(window, len(bars) - 1):
        signal = signal_for(closes, index, window)
        bar = bars[index + 1]
        execution_price = float(bar["open"])

        if signal == "sell" and units > 0:
            sold_units = units
            fee = sold_units * execution_price * fee_rate
            cash += sold_units * execution_price - fee
            units = 0.0
            record("sell", bar, execution_price, sold_units, fee)
        elif signal == "buy" and units == 0:
            quantity = min(max_units, max_order_value / execution_price)
            quantity = min(quantity, cash / (execution_price * (1 + fee_rate)))
            notional = quantity * execution_price
            fee = notional * fee_rate
            if quantity > 0 and notional <= max_order_value and notional + fee <= cash:
                cash -= notional + fee
                units = quantity
                record("buy", bar, execution_price, quantity, fee)

        mark_price = float(bar["close"])
        equity = cash + units * mark_price
        peak_equity = max(peak_equity, equity)
        drawdown = peak_equity - equity
        maximum_drawdown_seen = max(maximum_drawdown_seen, drawdown)
        if drawdown >= max_drawdown:
            stopped_for_risk = True
            break

    if units > 0:
        final_bar = bars[-1]
        final_price = float(final_bar["close"])
        fee = units * final_price * fee_rate
        sold_units = units
        cash += sold_units * final_price - fee
        units = 0.0
        record("end_of_replay_sell", final_bar, final_price, sold_units, fee)

    return {
        "initial_cash": round(float(initial_cash), 8),
        "final_cash": round(cash, 8),
        "net_pnl": round(cash - initial_cash, 8),
        "trade_events": len(events),
        "max_drawdown": round(maximum_drawdown_seen, 8),
        "stopped_for_risk": stopped_for_risk,
        "live_trading": False,
        "events": events,
    }


def main():
    logging.basicConfig(filename="paper_bot.log", level=logging.INFO, encoding="utf-8")
    report = run_paper_bot(load_bars())
    print(
        f"Offline paper replay: net P&L={report['net_pnl']:.4f}, "
        f"events={report['trade_events']}, live_trading={report['live_trading']}"
    )
    print("Detailed events are recorded in paper_bot.log")


if __name__ == "__main__":
    main()
