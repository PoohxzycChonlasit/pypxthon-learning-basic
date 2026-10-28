def paper_equity_after_trade(entry, exit, quantity):
    return 100+(exit-entry)*quantity-(entry+exit)*quantity*.001
