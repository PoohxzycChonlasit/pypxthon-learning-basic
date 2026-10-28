def parse_positive_amount(text):
    # TODO: แปลง float และตรวจค่าติดลบ
    raise NotImplementedError("เติมการตรวจ input")

if __name__ == "__main__":
    raw = input()
    amount = parse_positive_amount(raw)
    print("INVALID" if amount is None else f"{amount:.2f}")
