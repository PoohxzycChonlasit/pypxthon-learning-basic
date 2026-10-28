def expected_trade_result(win_probability, average_win, average_loss):
    return win_probability * average_win + (1 - win_probability) * average_loss
