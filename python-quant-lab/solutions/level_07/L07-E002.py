def population_variance(values):
    return sum((x-sum(values)/len(values))**2 for x in values)/len(values) if values else 0
