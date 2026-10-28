def parse_positive_amount(text):
    try:
        amount = float(text)
    except ValueError:
        return None
    if amount < 0:
        return None
    return amount

if __name__ == "__main__":
    raw = input()
    amount = parse_positive_amount(raw)
    print("INVALID" if amount is None else f"{amount:.2f}")
