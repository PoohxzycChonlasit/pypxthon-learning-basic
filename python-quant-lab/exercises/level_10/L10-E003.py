def order_allowed(cash, quantity, price, max_order_value):
    # TODO: ตรวจ invariant ทุกข้อก่อนอนุญาต
    raise NotImplementedError("เติม risk check")

if __name__ == "__main__":
    cash = float(input())
    quantity = float(input())
    price = float(input())
    max_order_value = float(input())
    print(order_allowed(cash, quantity, price, max_order_value))
