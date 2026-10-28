def structured_event_log(event):
    return {'event':event.get('id'),'side':event.get('side'),'paper_only':True}
