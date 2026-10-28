def risk_sized_quantity(entry, exit, quantity):
    return 1/abs(entry-exit) if entry!=exit else 0
