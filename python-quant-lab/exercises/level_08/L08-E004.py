def net_trade_pnl(entry, exit_price, quantity, fee_rate):
    raise NotImplementedError("ดูเครื่องหมายผิดใน main")

if __name__ == "__main__":
    entry = float(input())
    exit_price = float(input())
    quantity = float(input())
    fee_rate = float(input())
    gross = (exit_price - entry) * quantity
    fee = (entry + exit_price) * quantity * fee_rate
    # BUG: fee เป็นค่าใช้จ่าย แต่กลับบวกเข้ากำไร
    print(gross + fee)
