def paper_step(state, event, max_order_value, fee_rate):
    cash = float(state["cash"])
    units = float(state["units"])
    quantity = float(event["quantity"])
    price = float(event["price"])
    side = event["side"]
    notional = quantity * price
    valid = (cash >= 0 and units >= 0 and quantity > 0 and price > 0
             and fee_rate >= 0 and notional <= max_order_value)
    accepted = False
    if valid and side == "buy" and notional * (1 + fee_rate) <= cash:
        cash -= notional * (1 + fee_rate)
        units += quantity
        accepted = True
    elif valid and side == "sell" and quantity <= units:
        cash += notional * (1 - fee_rate)
        units -= quantity
        accepted = True
    return {"accepted": accepted, "cash": cash if accepted else state["cash"],
            "units": units if accepted else state["units"], "live_trading": False}

if __name__ == "__main__":
    import json
    payload = json.loads(input())
    result = paper_step(payload["state"], payload["event"], payload["max_order_value"], payload["fee_rate"])
    print(f"accepted={result['accepted']} cash={result['cash']:.2f} units={result['units']:.2f} live_trading={result['live_trading']}")
