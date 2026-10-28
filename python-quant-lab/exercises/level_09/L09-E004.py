# L09-E004 — แก้ look-ahead ในค่าเฉลี่ยย้อนหลัง
# Level 9 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L09-E004
# macOS: python3.12 -B practice.py check L09-E004
# อ่านก่อนทำ: lessons/L09-E004.md

def trailing_mean(values, index, window):
    raise NotImplementedError("ดู look-ahead ใน main")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    # BUG: รวมค่าปัจจุบันและหารด้วย window + 1
    section = values[index - window:index + 1]
    print(sum(section) / len(section) if len(section) == window + 1 else "NONE")
