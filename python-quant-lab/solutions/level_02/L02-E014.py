def separate_gains_and_losses(values):
    return ([x for x in values if x>0],[x for x in values if x<0])
