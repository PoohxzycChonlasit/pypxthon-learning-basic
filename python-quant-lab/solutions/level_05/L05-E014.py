def count_repeated_symbols(text):
    return {s:text.upper().split(',').count(s) for s in set(text.upper().split(',')) if s}
