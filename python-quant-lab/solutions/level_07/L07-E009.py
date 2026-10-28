import math
def standard_score_last_value(values):
    import math; m=sum(values)/len(values); s=math.sqrt(sum((x-m)**2 for x in values)/len(values)); return (values[-1]-m)/s if values and s else None
