def final_offline_bot_assessment(event):
    return {'orders':1 if event.get('quantity',0)>0 else 0,'cash_after':event.get('cash',0)-event.get('quantity',0)*event.get('price',0) if event.get('side')=='buy' else event.get('cash',0),'live_trading':False}
