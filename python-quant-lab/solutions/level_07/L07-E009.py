import math

def standard_score_last_value(values):
    if not values:
        return None
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    standard_deviation = math.sqrt(variance)
    if standard_deviation == 0:
        return None
    return (values[-1] - mean) / standard_deviation
