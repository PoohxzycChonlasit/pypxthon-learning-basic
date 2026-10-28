def order_state(event):
    return 'accepted' if event.get('quantity',0)>0 else 'rejected'
