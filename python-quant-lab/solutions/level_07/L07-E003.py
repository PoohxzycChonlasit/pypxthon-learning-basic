import math
def population_standard_deviation(values):
    import math; return math.sqrt(sum((x-sum(values)/len(values))**2 for x in values)/len(values)) if values else 0
