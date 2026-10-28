def slippage_adjusted_exit(exit_price, slippage_rate):
    return exit_price * (1 - slippage_rate)
