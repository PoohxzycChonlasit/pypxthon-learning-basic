def positive_observation_count(values):
    return sum(x is not None and x>0 for x in values)
