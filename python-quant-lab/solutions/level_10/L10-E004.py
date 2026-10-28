def valid_bar(bar):
    prices = [bar["open"], bar["high"], bar["low"], bar["close"]]
    if any(price <= 0 for price in prices) or bar["volume"] < 0:
        return False
    return (bar["high"] >= max(bar["open"], bar["close"])
            and bar["low"] <= min(bar["open"], bar["close"])
            and bar["low"] <= bar["high"])

if __name__ == "__main__":
    import json
    bar = json.loads(input())
    print(valid_bar(bar))
