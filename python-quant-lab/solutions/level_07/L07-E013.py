def mean_absolute_deviation(values):
    return sum(abs(x-sum(values)/len(values)) for x in values)/len(values) if values else 0
