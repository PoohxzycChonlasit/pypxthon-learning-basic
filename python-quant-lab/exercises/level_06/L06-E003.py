# L06-E003 — เติม rolling mean ตามหน้าต่าง
# Level 6 · Tier 3 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L06-E003
# macOS: python3.12 -B practice.py check L06-E003
# อ่านก่อนทำ: lessons/L06-E003.md

def rolling_means(values, window):
    # TODO: คืนค่าเฉลี่ยของแต่ละ slice ที่ยาว window
    raise NotImplementedError("เติม rolling window")

if __name__ == "__main__":
    values = [float(value) for value in input().split()]
    window = int(input())
    print(rolling_means(values, window))
