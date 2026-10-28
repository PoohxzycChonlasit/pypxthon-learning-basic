def cumulative_sum(values):
    return [sum(values[:i+1]) for i in range(len(values))]
