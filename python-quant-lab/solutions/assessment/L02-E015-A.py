def final_loop_assessment(values):
    return {'count':len(values),'positive':sum(x>0 for x in values),'net':sum(values)}
