import math

def restore_cash_state(event):
    cash = event.get("cash", 100.0)
    if isinstance(cash, bool) or not isinstance(cash, (int, float)):
        return 100.0
    if not math.isfinite(cash) or cash < 0:
        return 100.0
    return cash
