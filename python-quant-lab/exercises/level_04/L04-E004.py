# L04-E004 — แก้การตรวจหารด้วยศูนย์
# Level 4 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L04-E004
# macOS: python3.12 -B practice.py check L04-E004
# อ่านก่อนทำ: lessons/L04-E004.md

def safe_division(numerator, denominator):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    numerator = float(input())
    denominator = float(input())
    # BUG: ตรวจ numerator แทน denominator
    if numerator == 0:
        result = None
    else:
        result = numerator / denominator
    print("NONE" if result is None else result)
