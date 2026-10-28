def sum_until_budget_limit(values):
    return next((sum(values[:i+1]) for i in range(len(values)) if sum(values[:i+1])>=10),sum(values))
