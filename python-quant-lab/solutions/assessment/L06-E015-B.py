def final_data_cleaning_assessment(values):
    filled = []
    filled_count = 0
    last_value = None
    for value in values:
        if value is None:
            if last_value is None:
                filled.append(None)
            else:
                filled.append(last_value)
                filled_count += 1
        else:
            last_value = value
            filled.append(value)
    return {"filled": filled, "filled_count": filled_count}
