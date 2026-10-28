def remove_blank_fields(text):
    return [x.strip() for x in text.split(',') if x.strip()]
