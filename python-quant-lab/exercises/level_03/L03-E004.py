# L03-E004 — แก้การลบรายการซ้ำโดยรักษาลำดับ
# Level 3 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L03-E004
# macOS: python3.12 -B practice.py check L03-E004
# อ่านก่อนทำ: lessons/L03-E004.md

def unique_in_order(items):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    items = input().split(",")
    # BUG: sorting removes duplicates but changes first-seen order
    print(sorted(set(items)))
