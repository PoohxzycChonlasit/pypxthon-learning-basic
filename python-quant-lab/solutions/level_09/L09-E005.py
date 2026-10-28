def crossover_booleans(values):
    return [b>a for a,b in zip(values,values[1:])]
