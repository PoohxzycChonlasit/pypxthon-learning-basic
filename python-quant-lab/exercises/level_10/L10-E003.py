# L10-E003 — เติม validator ของ paper order
# Level 10 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L10-E003
# macOS: python3.12 -B practice.py check L10-E003
# อ่านก่อนทำ: lessons/L10-E003.md

def order_allowed(cash, quantity, price, max_order_value):
    # TODO: ตรวจ invariant ทุกข้อก่อนอนุญาต
    raise NotImplementedError("เติม risk check")

if __name__ == "__main__":
    cash = float(input())
    quantity = float(input())
    price = float(input())
    max_order_value = float(input())
    print(order_allowed(cash, quantity, price, max_order_value))
