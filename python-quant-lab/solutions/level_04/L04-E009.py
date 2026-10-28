def risk_based_units(x, y):
    return x/abs(y) if y else 0
