# L02-E004 — แก้เกณฑ์ส่งฟรีที่ขอบเขต
# Level 2 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L02-E004
# macOS: python3.12 -B practice.py check L02-E004
# อ่านก่อนทำ: lessons/L02-E004.md

def shipping_fee(order_total):
    raise NotImplementedError("ดูโค้ดที่พังใน main")

if __name__ == "__main__":
    order_total = float(input())
    # BUG: เงื่อนไขและค่าค่าส่งผิด
    fee = 0 if order_total > 500 else 0
    print(int(fee))
