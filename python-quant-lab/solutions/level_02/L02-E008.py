def maximum_drawdown_step(values):
    return min((b/a-1 for a,b in zip(values,values[1:]) if a),default=0)
