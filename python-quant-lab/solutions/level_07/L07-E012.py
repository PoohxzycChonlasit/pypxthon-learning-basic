def count_above_median(values):
    return sum(x>sorted(values)[len(values)//2] for x in values) if values else 0
