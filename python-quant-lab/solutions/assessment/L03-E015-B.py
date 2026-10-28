def final_structure_assessment(items):
    return {'length':len(items),'first':items[0] if items else None,'unique':len(set(items))}
