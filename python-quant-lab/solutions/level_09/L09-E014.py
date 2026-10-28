def net_returns_after_costs(returns, fee_rate, slippage_rate, funding_rate):
    total_cost = fee_rate + slippage_rate + funding_rate
    return [value - total_cost for value in returns]
