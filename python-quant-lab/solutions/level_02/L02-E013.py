def sum_until_budget_limit(values):
    budget = 10
    total = 0
    for amount in values:
        if total + amount > budget:
            break
        total += amount
    return total
