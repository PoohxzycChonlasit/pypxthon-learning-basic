def validate_numeric_text(text):
    return text.replace('.','',1).isdigit()
