def drawdown_fraction(peak_equity, current_equity):
    if peak_equity <= 0:
        return 0
    return max(0, (peak_equity - current_equity) / peak_equity)
