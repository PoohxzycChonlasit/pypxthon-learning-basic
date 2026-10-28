def order_allowed(cash, quantity, price, max_order_value):
    if cash < 0 or quantity <= 0 or price <= 0 or max_order_value <= 0:
        return False
    notional = quantity * price
    return notional <= max_order_value and notional <= cash

if __name__ == "__main__":
    cash = float(input())
    quantity = float(input())
    price = float(input())
    max_order_value = float(input())
    print(order_allowed(cash, quantity, price, max_order_value))
