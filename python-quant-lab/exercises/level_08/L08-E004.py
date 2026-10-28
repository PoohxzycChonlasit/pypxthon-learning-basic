# L08-E004 — แก้สูตรที่บวก fee เข้ากำไร
# Level 8 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L08-E004
# macOS: python3.12 -B practice.py check L08-E004
# อ่านก่อนทำ: lessons/L08-E004.md

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
