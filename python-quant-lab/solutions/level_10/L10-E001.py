import math

def _valid_nonnegative_number(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value >= 0)

def validate_paper_order(event):
    if not isinstance(event, dict):
        return False
    side = event.get("side")
    quantity = event.get("quantity")
    price = event.get("price")
    cash = event.get("cash")
    if side not in ("buy", "sell"):
        return False
    if not _valid_nonnegative_number(quantity) or quantity <= 0:
        return False
    if not _valid_nonnegative_number(price) or price <= 0:
        return False
    if not _valid_nonnegative_number(cash):
        return False
    return side == "sell" or quantity * price <= cash
