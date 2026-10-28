def identify_future_leakage(values):
    return any(feature_time>=target_time for feature_time,target_time in values)
