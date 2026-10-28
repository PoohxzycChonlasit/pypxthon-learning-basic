# L02-E003 — เติมลูปกรองงบประมาณ
# Level 2 · Tier 1 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L02-E003
# macOS: python3.12 -B practice.py check L02-E003
# อ่านก่อนทำ: lessons/L02-E003.md

def sum_at_or_below_limit(values, limit):
    # TODO: วน values และคืนผลรวมที่ผ่านเงื่อนไข
    raise NotImplementedError("เติมลูป")

if __name__ == "__main__":
    limit = int(input())
    values = [int(value) for value in input().split()]
    print(sum_at_or_below_limit(values, limit))
