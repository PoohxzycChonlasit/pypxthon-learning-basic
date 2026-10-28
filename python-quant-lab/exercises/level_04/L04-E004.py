def safe_division(numerator, denominator):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    numerator = float(input())
    denominator = float(input())
    # BUG: ตรวจ numerator แทน denominator
    if numerator == 0:
        result = None
    else:
        result = numerator / denominator
    print("NONE" if result is None else result)
