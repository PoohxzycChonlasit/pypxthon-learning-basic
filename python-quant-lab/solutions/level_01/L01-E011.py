buy_price = float(input())
sell_price = float(input())
quantity = float(input())
gross_profit = (sell_price - buy_price) * quantity
print(f"{gross_profit:.2f}")
