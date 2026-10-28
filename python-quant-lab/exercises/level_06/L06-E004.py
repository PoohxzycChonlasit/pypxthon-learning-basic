# L06-E004 — แก้การเติม missing ด้วยค่าก่อนหน้า
# Level 6 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L06-E004
# macOS: python3.12 -B practice.py check L06-E004
# อ่านก่อนทำ: lessons/L06-E004.md

raw = input().strip()
values = [] if not raw else [None if x == "NA" else float(x) for x in raw.split(",")]
# BUG: every missing observation is replaced with zero.
clean = [0 if value is None else value for value in values]
print(clean)
