def validate_paper_order(event):
    return event.get('quantity',0)>0 and event.get('price',0)>0
