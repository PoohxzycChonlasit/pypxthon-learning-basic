def record_order_result(event):
    return {'id':event.get('id'),'status':'paper','live':False}
