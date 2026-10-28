def parse_key_value(text):
    return dict(part.split('=',1) for part in text.split(';') if '=' in part)
