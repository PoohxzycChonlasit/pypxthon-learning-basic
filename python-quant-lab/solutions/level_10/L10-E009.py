import math

def safe_default_fee(event):
    fee = event.get("fee", 0.0)
    if isinstance(fee, bool) or not isinstance(fee, (int, float)):
        return 0.0
    if not math.isfinite(fee) or fee < 0:
        return 0.0
    return fee
