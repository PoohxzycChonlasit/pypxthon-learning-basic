def parse_delimited_numbers(text):
    return [float(x) for x in text.split(',') if x.strip()]
