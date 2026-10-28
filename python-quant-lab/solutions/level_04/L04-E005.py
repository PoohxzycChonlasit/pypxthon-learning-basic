def invoice_total(subtotal, discount_rate, tax_rate):
    if subtotal < 0 or not 0 <= discount_rate <= 1 or not 0 <= tax_rate <= 1:
        return None
    discounted = subtotal * (1 - discount_rate)
    return discounted * (1 + tax_rate)

if __name__ == "__main__":
    subtotal = float(input())
    discount_rate = float(input())
    tax_rate = float(input())
    result = invoice_total(subtotal, discount_rate, tax_rate)
    print("INVALID" if result is None else f"{result:.2f}")
