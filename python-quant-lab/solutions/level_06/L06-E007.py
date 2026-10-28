def select_above_average(values):
    return [x for x in values if x is not None and x>sum(v for v in values if v is not None)/len([v for v in values if v is not None])] if any(v is not None for v in values) else []
