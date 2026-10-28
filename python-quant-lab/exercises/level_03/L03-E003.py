# L03-E003 — เติมตารางนับรหัสสินค้า
# Level 3 · Tier 1 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L03-E003
# macOS: python3.12 -B practice.py check L03-E003
# อ่านก่อนทำ: lessons/L03-E003.md

def frequency_table(tags):
    # TODO: คืน dict ที่ map tag ไปยังจำนวนครั้ง
    raise NotImplementedError("เติมตัวนับ")

if __name__ == "__main__":
    raw = input().strip()
    tags = raw.split(",") if raw else []
    print(sorted(frequency_table(tags).items()))
