def risk_floor_stop(event):
    return event.get("cash", 0) <= event.get("risk_floor", 0)
