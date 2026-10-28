# L07-E003 — เติมสูตร population variance
# Level 7 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L07-E003
# macOS: python3.12 -B practice.py check L07-E003
# อ่านก่อนทำ: lessons/L07-E003.md

def population_variance(values):
    # TODO: mean แล้วหาค่าเฉลี่ย squared deviations
    raise NotImplementedError("เติมสูตร variance")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    result = population_variance(values)
    print("NONE" if result is None else result)
