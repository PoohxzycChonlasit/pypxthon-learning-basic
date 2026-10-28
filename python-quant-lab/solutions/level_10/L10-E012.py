def loss_limit_stop(event):
    return event.get('day_pnl',0)<=-abs(event.get('loss_limit',0))
