def risk_reward_ratio(entry, target, stop):
    risk = abs(entry - stop)
    return abs(target - entry) / risk if risk else None
