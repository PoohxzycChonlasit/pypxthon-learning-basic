def find_first_threshold(values):
    return next((i for i,x in enumerate(values) if x>=3),-1)
