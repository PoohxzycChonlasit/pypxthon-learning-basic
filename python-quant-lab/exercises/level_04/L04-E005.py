# L04-E005 — สร้างยอดใบแจ้งหนี้หลังส่วนลดและภาษี
# Level 4 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L04-E005
# macOS: python3.12 -B practice.py check L04-E005
# อ่านก่อนทำ: lessons/L04-E005.md

def invoice_total(subtotal, discount_rate, tax_rate):
    raise NotImplementedError("TODO: ตรวจค่าและคำนวณยอด")

if __name__ == "__main__":
    subtotal = float(input())
    discount_rate = float(input())
    tax_rate = float(input())
    result = invoice_total(subtotal, discount_rate, tax_rate)
    print("INVALID" if result is None else f"{result:.2f}")
