def final_data_cleaning_assessment(values):
    return {'clean': [x for x in values if x is not None], 'missing':sum(x is None for x in values)}
