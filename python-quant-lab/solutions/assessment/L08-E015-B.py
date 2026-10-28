def final_paper_risk_assessment(entry, exit, quantity):
    gross = (exit - entry) * quantity
    return_percent = (exit - entry) / entry * 100 if entry != 0 else None
    if exit > entry:
        direction = "up"
    elif exit < entry:
        direction = "down"
    else:
        direction = "flat"
    return {"gross": gross, "return_percent": return_percent, "direction": direction, "live_trading": False}
