# L05-E003 — เติมตัวแปลงจำนวนเงินแบบปลอดภัย
# Level 5 · Tier 1 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L05-E003
# macOS: python3.12 -B practice.py check L05-E003
# อ่านก่อนทำ: lessons/L05-E003.md

def parse_positive_amount(text):
    # TODO: แปลง float และตรวจค่าติดลบ
    raise NotImplementedError("เติมการตรวจ input")

if __name__ == "__main__":
    raw = input()
    amount = parse_positive_amount(raw)
    print("INVALID" if amount is None else f"{amount:.2f}")
