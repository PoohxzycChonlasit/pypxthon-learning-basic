def two_period_sma(values):
    return [(values[i-1]+values[i])/2 for i in range(1,len(values))]
