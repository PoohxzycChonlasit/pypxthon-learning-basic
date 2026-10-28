gross = float(input())
fee_percent = float(input())
fee = abs(gross) * fee_percent / 100
net = gross - fee
print(f"{net:.2f}")
