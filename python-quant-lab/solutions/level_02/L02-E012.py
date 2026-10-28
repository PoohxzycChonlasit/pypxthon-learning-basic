def count_consecutive_rises(values):
    return sum(b>a for a,b in zip(values,values[1:]))
