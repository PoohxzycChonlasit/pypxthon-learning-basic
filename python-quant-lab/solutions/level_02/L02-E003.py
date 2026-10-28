def classify_each_result(values):
    return ['profit' if x>0 else 'loss' if x<0 else 'flat' for x in values]
