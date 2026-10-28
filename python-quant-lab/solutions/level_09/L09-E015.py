def final_research_decision(values):
    return {'observations':len(values),'mean':sum(values)/len(values) if values else None,'decision':'evaluate out of sample' if len(values)>=3 else 'insufficient data'}
