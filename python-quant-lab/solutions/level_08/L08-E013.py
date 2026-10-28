def drawdown_fraction(entry, exit, quantity):
    return (exit-entry)/entry if entry else 0
