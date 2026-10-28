def safe_parse_amount(text):
    parts = text.split(",")
    if len(parts) != 2:
        return None
    try:
        return float(parts[1].strip())
    except ValueError:
        return None
