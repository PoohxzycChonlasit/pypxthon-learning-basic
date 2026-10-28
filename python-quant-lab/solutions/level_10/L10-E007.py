def paper_exposure(event):
    return event.get('quantity',0)*event.get('price',0)
