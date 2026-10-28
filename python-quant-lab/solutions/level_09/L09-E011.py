def threshold_signals(prices, minimum_return):
    return [int(previous > 0 and current > previous * (1 + minimum_return))
            for previous, current in zip(prices, prices[1:])]
