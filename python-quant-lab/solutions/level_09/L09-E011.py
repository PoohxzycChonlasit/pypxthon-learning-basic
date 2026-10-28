def threshold_signals(values):
    return [1 if b>a else 0 for a,b in zip(values,values[1:])]
