def final_parsing_assessment(text):
    return {'fields':len(text.split(',')),'normalized':text.strip().upper()}
