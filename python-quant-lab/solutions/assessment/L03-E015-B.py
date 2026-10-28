def final_structure_assessment(items):
    seen = set()
    unique_items = []
    duplicate_count = 0
    for item in items:
        if item in seen:
            duplicate_count += 1
        else:
            seen.add(item)
            unique_items.append(item)
    return {"unique_items": unique_items, "duplicate_count": duplicate_count}
