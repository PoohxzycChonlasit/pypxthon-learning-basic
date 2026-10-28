def risk_reward_ratio(entry, exit, quantity):
    return abs(exit-entry)/abs(entry-exit) if entry!=exit else None
