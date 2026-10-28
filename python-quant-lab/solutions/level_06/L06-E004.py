def rolling_two_point_mean(values):
    return [(a+b)/2 for a,b in zip(values,values[1:]) if a is not None and b is not None]
