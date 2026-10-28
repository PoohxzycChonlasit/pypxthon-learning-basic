def idempotency_check(event):
    return event.get('id') not in event.get('seen',[])
