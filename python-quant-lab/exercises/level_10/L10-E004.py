# L10-E004 — แก้ validator OHLC ที่ตรวจไม่ครบ
# Level 10 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L10-E004
# macOS: python3.12 -B practice.py check L10-E004
# อ่านก่อนทำ: lessons/L10-E004.md

def valid_bar(bar):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    import json
    bar = json.loads(input())
    # BUG: high >= low ไม่ได้ตรวจเทียบ open และ close
    valid = bar["high"] >= bar["low"] and bar["volume"] >= 0
    print(valid)
