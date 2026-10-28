# L05-E005 — สรุปยอดขายพร้อมนับแถวเสีย
# Level 5 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L05-E005
# macOS: python3.12 -B practice.py check L05-E005
# อ่านก่อนทำ: lessons/L05-E005.md

def sales_report(lines):
    raise NotImplementedError("TODO: parse, validate, and total rows")

if __name__ == "__main__":
    import sys
    report = sales_report(sys.stdin.read().splitlines())
    print(f"valid={report['valid']} rejected={report['rejected']} revenue={report['revenue']:.2f}")
