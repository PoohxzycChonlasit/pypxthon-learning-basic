def rolling_maximum(values):
    return [max(values[i-1:i+1]) for i in range(1,len(values)) if None not in values[i-1:i+1]]
