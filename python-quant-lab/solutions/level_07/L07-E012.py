from statistics import median

def count_above_median(values):
    if not values:
        return 0
    midpoint = median(values)
    return sum(value > midpoint for value in values)
