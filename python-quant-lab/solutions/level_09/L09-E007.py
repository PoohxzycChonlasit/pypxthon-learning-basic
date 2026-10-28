def gross_signal_returns(values):
    return [signal*(b/a-1) for a,b,signal in zip(values,values[1:], [1]*(len(values)-1)) if a]
