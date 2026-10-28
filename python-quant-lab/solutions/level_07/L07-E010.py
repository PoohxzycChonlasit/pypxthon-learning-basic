import math
def log_returns(values):
    import math; return [math.log(b/a) for a,b in zip(values,values[1:]) if a>0 and b>0]
