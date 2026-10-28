def rolling_mean(values):
    return [(values[i-1]+values[i]+values[i+1])/3 for i in range(1,len(values)-1)]
