import math

def final_offline_bot_assessment(event):
    if not isinstance(event, dict):
        return {"accepted": False, "cash_after": 0, "position_after": 0, "live_trading": False}
    try:
        cash = float(event.get("cash", 0))
        position = float(event.get("position", 0))
        quantity = float(event.get("quantity", 0))
        price = float(event.get("price", 0))
    except (TypeError, ValueError):
        return {"accepted": False, "cash_after": 0, "position_after": 0, "live_trading": False}
    valid = all(math.isfinite(x) for x in (cash, position, quantity, price))
    valid = valid and cash >= 0 and position >= 0 and quantity > 0 and price > 0
    valid = valid and event.get("side") == "sell" and position >= quantity
    if not valid:
        return {"accepted": False, "cash_after": cash, "position_after": position, "live_trading": False}
    return {"accepted": True, "cash_after": cash + quantity * price, "position_after": position - quantity, "live_trading": False}
