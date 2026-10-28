# L08-E005 — ตรวจ exposure รวมของพอร์ตจำลอง
# Level 8 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L08-E005
# macOS: python3.12 -B practice.py check L08-E005
# อ่านก่อนทำ: lessons/L08-E005.md

def exposure_report(equity, positions, max_fraction):
    raise NotImplementedError("TODO: ตรวจและรวม exposure")

if __name__ == "__main__":
    import json
    equity = float(input())
    positions = json.loads(input())
    max_fraction = float(input())
    report = exposure_report(equity, positions, max_fraction)
    if report is None:
        print("INVALID")
    else:
        limit = equity * max_fraction
        print(f"exposure={report['exposure']:.2f} limit={limit:.2f} allowed={report['allowed']}")
