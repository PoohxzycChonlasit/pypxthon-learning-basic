def maximum_drawdown_step(values):
    declines = [
        current / previous - 1
        for previous, current in zip(values, values[1:])
        if previous != 0 and current / previous - 1 < 0
    ]
    return min(declines, default=0)
