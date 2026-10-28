def net_trade_pnl(entry, exit_price, quantity, fee_rate):
    gross = (exit_price - entry) * quantity
    fee = (entry + exit_price) * quantity * fee_rate
    return gross - fee

if __name__ == "__main__":
    entry = float(input())
    exit_price = float(input())
    quantity = float(input())
    fee_rate = float(input())
    print(net_trade_pnl(entry, exit_price, quantity, fee_rate))
