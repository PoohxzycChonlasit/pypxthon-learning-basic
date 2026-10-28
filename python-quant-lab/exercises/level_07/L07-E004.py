# L07-E004 — แก้เศษส่วน conversion rate
# Level 7 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L07-E004
# macOS: python3.12 -B practice.py check L07-E004
# อ่านก่อนทำ: lessons/L07-E004.md

def conversion_rate(signups, visits):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    signups = float(input())
    visits = float(input())
    # BUG: เศษส่วนกลับด้านและตรวจตัวตั้ง
    rate = None if signups == 0 else visits / signups
    print("NONE" if rate is None else rate)
