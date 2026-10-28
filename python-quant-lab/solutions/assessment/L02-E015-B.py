def final_loop_assessment(values):
    even_sum = 0
    negative_count = 0
    for value in values:
        if value % 2 == 0:
            even_sum += value
        if value < 0:
            negative_count += 1
    return {"even_sum": even_sum, "negative_count": negative_count}
