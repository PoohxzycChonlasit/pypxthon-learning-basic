def shipping_fee(order_total):
    raise NotImplementedError("ดูโค้ดที่พังใน main")

if __name__ == "__main__":
    order_total = float(input())
    # BUG: เงื่อนไขและค่าค่าส่งผิด
    fee = 0 if order_total > 500 else 0
    print(int(fee))
