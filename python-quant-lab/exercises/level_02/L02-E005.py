# L02-E005 — คำนวณยอดสุทธิพร้อมค่าส่งตามเขต
# Level 2 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L02-E005
# macOS: python3.12 -B practice.py check L02-E005
# อ่านก่อนทำ: lessons/L02-E005.md

def final_order_amount(subtotal, zone):
    raise NotImplementedError("TODO: ตรวจยอดและเลือกค่าส่ง")

if __name__ == "__main__":
    subtotal = float(input())
    zone = input().strip()
    result = final_order_amount(subtotal, zone)
    if result is None:
        print("INVALID")
    else:
        print(f"{result:.2f}")
