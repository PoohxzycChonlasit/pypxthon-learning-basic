def benchmark_buy_hold(values):
    return values[-1]/values[0]-1 if len(values)>1 and values[0] else None
