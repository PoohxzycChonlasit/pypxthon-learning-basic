import math

def position_update(event):
    quantity = event.get("quantity", 0)
    if (not isinstance(quantity, (int, float)) or isinstance(quantity, bool)
            or not math.isfinite(quantity) or quantity < 0):
        return 0
    if event.get("side") == "buy":
        return quantity
    if event.get("side") == "sell":
        return -quantity
    return 0
