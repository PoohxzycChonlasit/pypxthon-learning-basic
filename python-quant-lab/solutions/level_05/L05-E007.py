def format_log_row(text):
    return ','.join(part.strip() for part in text.split(','))
