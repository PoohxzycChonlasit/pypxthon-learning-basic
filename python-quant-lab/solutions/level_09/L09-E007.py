def gross_signal_returns(prices, signals):
    return [signal * (current / previous - 1)
            for previous, current, signal in zip(prices, prices[1:], signals)
            if previous > 0]
