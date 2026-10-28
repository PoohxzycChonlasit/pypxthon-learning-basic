def simulate_sell_cash(event):
    return event['cash']+event['quantity']*event['price'] if event.get('side')=='sell' else event['cash']
