# L05-E004 — แก้ตัวนับช่อง CSV ที่มี comma ใน quote
# Level 5 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L05-E004
# macOS: python3.12 -B practice.py check L05-E004
# อ่านก่อนทำ: lessons/L05-E004.md

def csv_field_count(line):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    line = input()
    # BUG: comma ใน quoted field ไม่ใช่ตัวแบ่งคอลัมน์
    print(len(line.split(",")))
