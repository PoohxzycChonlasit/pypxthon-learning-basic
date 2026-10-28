def safe_default_fee(event):
    return event.get('fee',0.0)
