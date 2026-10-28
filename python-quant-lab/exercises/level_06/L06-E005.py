# L06-E005 — สรุปรายได้แยกตามสินค้า
# Level 6 · Tier 4 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L06-E005
# macOS: python3.12 -B practice.py check L06-E005
# อ่านก่อนทำ: lessons/L06-E005.md

def revenue_by_product(rows):
    raise NotImplementedError("TODO: รวมรายได้ตาม product")

if __name__ == "__main__":
    import csv
    import sys
    rows = list(csv.DictReader(sys.stdin))
    report = revenue_by_product(rows)
    if not report:
        print("NONE")
    else:
        for product in sorted(report):
            print(f"{product}:{report[product]:.2f}")
