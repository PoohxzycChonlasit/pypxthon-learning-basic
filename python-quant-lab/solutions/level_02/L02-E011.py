def stop_at_first_loss(values):
    return list(values[:next((i for i,x in enumerate(values) if x<0),len(values))])
