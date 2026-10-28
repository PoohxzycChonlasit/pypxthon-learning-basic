def position_update(event):
    return event.get('quantity',0) if event.get('side')=='buy' else -event.get('quantity',0)
