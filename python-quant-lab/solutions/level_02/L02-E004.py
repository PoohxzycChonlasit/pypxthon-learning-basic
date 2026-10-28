def shipping_fee(order_total):
    return 0 if order_total >= 500 else 40

if __name__ == "__main__":
    order_total = float(input())
    print(shipping_fee(order_total))
