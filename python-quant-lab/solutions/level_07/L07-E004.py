def median(values):
    return (sorted(values)[(len(values)-1)//2]+sorted(values)[len(values)//2])/2 if values else None
