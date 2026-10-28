def final_statistics_assessment(values):
    if not values:
        return {"median": None, "range": None}
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    return {"median": median, "range": ordered[-1] - ordered[0]}
