def final_order_amount(subtotal, zone):
    raise NotImplementedError("TODO: ตรวจยอดและเลือกค่าส่ง")

if __name__ == "__main__":
    subtotal = float(input())
    zone = input().strip()
    result = final_order_amount(subtotal, zone)
    if result is None:
        print("INVALID")
    else:
        print(f"{result:.2f}")
