# L04-E003 — เติมฟังก์ชันแปลงหน่วยค่าใช้จ่าย
# Level 4 · Tier 1 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L04-E003
# macOS: python3.12 -B practice.py check L04-E003
# อ่านก่อนทำ: lessons/L04-E003.md

def compose_adjustment(amount, scale, offset):
    # TODO: คืน amount * scale + offset
    raise NotImplementedError("เติมสูตร")

if __name__ == "__main__":
    amount = float(input())
    scale = float(input())
    offset = float(input())
    print(f"{compose_adjustment(amount, scale, offset):.1f}")
