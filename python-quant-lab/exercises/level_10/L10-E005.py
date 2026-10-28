# L10-E005 — จำลอง paper buy/sell พร้อม accounting invariant
# Level 10 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L10-E005
# macOS: python3.12 -B practice.py check L10-E005
# อ่านก่อนทำ: lessons/L10-E005.md

def paper_step(state, event, max_order_value, fee_rate):
    raise NotImplementedError("TODO: validate then update paper state")

if __name__ == "__main__":
    import json
    payload = json.loads(input())
    result = paper_step(payload["state"], payload["event"], payload["max_order_value"], payload["fee_rate"])
    print(f"accepted={result['accepted']} cash={result['cash']:.2f} units={result['units']:.2f} live_trading={result['live_trading']}")
