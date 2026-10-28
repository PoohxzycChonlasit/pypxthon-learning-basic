def positive_rate(values):
    return sum(x>0 for x in values)/len(values) if values else None
