def risk_sized_quantity(risk_budget, entry, stop):
    risk_per_unit = abs(entry - stop)
    return risk_budget / risk_per_unit if risk_per_unit else 0
