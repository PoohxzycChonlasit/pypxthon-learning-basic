buy = float(input())
sell = float(input())
quantity = float(input())
fee_percent = float(input())
gross = (sell - buy) * quantity
fees = (buy + sell) * quantity * fee_percent / 100
net = gross - fees
print(f"{net:.2f}")
