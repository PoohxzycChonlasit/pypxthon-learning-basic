def fill_missing_from_previous(values):
    return [next((values[j] for j in range(i,-1,-1) if values[j] is not None),None) for i in range(len(values))]
