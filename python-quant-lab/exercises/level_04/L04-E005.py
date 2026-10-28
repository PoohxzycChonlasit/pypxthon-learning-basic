def invoice_total(subtotal, discount_rate, tax_rate):
    raise NotImplementedError("TODO: ตรวจค่าและคำนวณยอด")

if __name__ == "__main__":
    subtotal = float(input())
    discount_rate = float(input())
    tax_rate = float(input())
    result = invoice_total(subtotal, discount_rate, tax_rate)
    print("INVALID" if result is None else f"{result:.2f}")
