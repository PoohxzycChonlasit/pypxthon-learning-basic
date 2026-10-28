def one_step_momentum(values):
    return [b/a-1 for a,b in zip(values,values[1:]) if a]
