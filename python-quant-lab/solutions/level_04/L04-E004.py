def safe_division(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator

if __name__ == "__main__":
    numerator = float(input())
    denominator = float(input())
    result = safe_division(numerator, denominator)
    print("NONE" if result is None else result)
