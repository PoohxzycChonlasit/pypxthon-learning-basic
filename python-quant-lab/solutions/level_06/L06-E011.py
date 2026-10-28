def demean_series(values):
    return [x-sum(values)/len(values) for x in values] if values else []
