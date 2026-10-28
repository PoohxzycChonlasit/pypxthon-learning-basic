def net_long_profit(entry, exit, quantity):
    return (exit-entry)*quantity-(entry+exit)*quantity*.001
