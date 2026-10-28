# L09-E003 — เติมค่าเฉลี่ยจากข้อมูลก่อน index
# Level 9 · Tier 1 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L09-E003
# macOS: python3.12 -B practice.py check L09-E003
# อ่านก่อนทำ: lessons/L09-E003.md

def prior_mean(values, index, window):
    # TODO: ใช้เฉพาะ slice ก่อน index
    raise NotImplementedError("เติมการเลือก window")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    result = prior_mean(values, index, window)
    print("NONE" if result is None else result)
