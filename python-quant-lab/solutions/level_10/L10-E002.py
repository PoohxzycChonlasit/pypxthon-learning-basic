def simulate_buy_cash(event):
    return event['cash']-event['quantity']*event['price'] if event.get('side')=='buy' else event['cash']
