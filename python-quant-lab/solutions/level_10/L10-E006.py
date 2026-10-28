def risk_floor_stop(event):
    return event.get('cash',0)<=0
