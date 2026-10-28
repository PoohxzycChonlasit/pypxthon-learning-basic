# L01-E014 — แก้บั๊กการหักค่าธรรมเนียมซื้อขาย
# Level 1 · Tier 4 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L01-E014
# macOS: python3.12 -B practice.py check L01-E014
# อ่านก่อนทำ: lessons/L01-E014.md

buy = float(input())
sell = float(input())
quantity = float(input())
fee_percent = float(input())
gross = (sell - buy) * quantity
fees = (buy + sell) * quantity * fee_percent / 100
net = gross + fees  # BUG: ค่าธรรมเนียมต้องถูกหัก
print(f"{net:.2f}")
