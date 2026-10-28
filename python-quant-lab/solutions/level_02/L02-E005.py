def final_order_amount(subtotal, zone):
    if subtotal < 0 or zone not in ("local", "remote"):
        return None
    if subtotal >= 300:
        fee = 0
    else:
        fee = 20 if zone == "local" else 50
    return subtotal + fee

if __name__ == "__main__":
    subtotal = float(input())
    zone = input().strip()
    result = final_order_amount(subtotal, zone)
    if result is None:
        print("INVALID")
    else:
        print(f"{result:.2f}")
