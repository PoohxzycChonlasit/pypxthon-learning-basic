def lag_series(values):
    return [None]+values[:-1] if values else []
