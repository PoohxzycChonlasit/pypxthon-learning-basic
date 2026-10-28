def build_running_totals(values):
    return [sum(values[:i+1]) for i in range(len(values))]
