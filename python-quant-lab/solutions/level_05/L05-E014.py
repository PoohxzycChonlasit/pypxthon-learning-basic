def count_repeated_symbols(text):
    counts = {}
    for token in text.split(","):
        symbol = token.strip().upper()
        if symbol:
            counts[symbol] = counts.get(symbol, 0) + 1
    return counts
