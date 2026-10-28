import math


def final_offline_bot_assessment(event):
    """Validate and account for one offline paper buy event."""
    if not isinstance(event, dict):
        return {"orders": 0, "cash_after": 0, "live_trading": False}

    original_cash = event.get("cash", 0)
    try:
        cash = float(original_cash)
        quantity = float(event.get("quantity", 0))
        price = float(event.get("price", 0))
    except (TypeError, ValueError):
        return {"orders": 0, "cash_after": original_cash, "live_trading": False}

    if not all(math.isfinite(value) for value in (cash, quantity, price)):
        return {"orders": 0, "cash_after": original_cash, "live_trading": False}
    if event.get("side") != "buy" or cash < 0 or quantity <= 0 or price <= 0:
        return {"orders": 0, "cash_after": cash, "live_trading": False}

    cost = quantity * price
    if cost > cash:
        return {"orders": 0, "cash_after": cash, "live_trading": False}
    return {"orders": 1, "cash_after": cash - cost, "live_trading": False}
