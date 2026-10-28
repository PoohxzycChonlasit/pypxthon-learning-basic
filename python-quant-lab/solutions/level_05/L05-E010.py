def detect_header_row(text):
    return text.lstrip().lower().startswith("date,")
