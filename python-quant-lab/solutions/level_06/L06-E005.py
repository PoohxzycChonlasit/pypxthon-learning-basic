def min_max_normalization(values):
    return [(x-min(values))/(max(values)-min(values)) for x in values] if values and max(values)!=min(values) else ([0.0]*len(values))
