def daily_returns(values):
    return [b/a-1 for a,b in zip(values,values[1:]) if a and b is not None]
