# L08-E003 — เติมการคำนวณขนาดสถานะจากวงเงินเสี่ยง
# Level 8 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L08-E003
# macOS: python3.12 -B practice.py check L08-E003
# อ่านก่อนทำ: lessons/L08-E003.md

def risk_based_quantity(equity, risk_percent, stop_distance):
    # TODO: ตรวจค่าก่อนหารและคืนขนาดหน่วย
    raise NotImplementedError("เติมสูตร position sizing")

if __name__ == "__main__":
    equity = float(input())
    risk_percent = float(input())
    stop_distance = float(input())
    print(f"{risk_based_quantity(equity, risk_percent, stop_distance):.2f}")
