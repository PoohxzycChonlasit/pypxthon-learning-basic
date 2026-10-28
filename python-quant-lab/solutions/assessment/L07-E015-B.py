def final_statistics_assessment(values):
    return {'mean':sum(values)/len(values) if values else None,'n':len(values),'min':min(values) if values else None,'max':max(values) if values else None}
