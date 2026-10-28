def restore_cash_state(event):
    return event.get('cash',100.0)
