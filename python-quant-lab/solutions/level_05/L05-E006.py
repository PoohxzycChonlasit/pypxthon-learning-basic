def safe_parse_amount(text):
    return float(text.split(',')[1]) if ',' in text else None
