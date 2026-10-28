import math

def final_research_decision(values):
    compound_return = math.prod(1 + value for value in values) - 1
    worst_period = min(values) if values else None
    return {"periods": len(values), "compound_return": compound_return, "worst_period": worst_period}
