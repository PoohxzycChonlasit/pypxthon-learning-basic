def split_into_positives_and_rest(items):
    return ([x for x in items if x>0],[x for x in items if x<=0])
