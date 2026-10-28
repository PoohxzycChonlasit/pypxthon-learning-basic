def reproducible_fold_boundaries(values):
    return [(i,min(i+2,len(values))) for i in range(0,len(values),2)]
