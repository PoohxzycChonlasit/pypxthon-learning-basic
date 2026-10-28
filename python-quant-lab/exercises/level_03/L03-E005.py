# L03-E005 — หา SKU ที่ควรเติมสต็อก
# Level 3 · Tier 2 · stdout
# แก้ TODO ในไฟล์นี้ให้แสดง output ตามโจทย์
# PowerShell: py -3.12 -B practice.py check L03-E005
# macOS: python3.12 -B practice.py check L03-E005
# อ่านก่อนทำ: lessons/L03-E005.md

def low_stock_skus(items, threshold):
    raise NotImplementedError("TODO: เลือกรหัสสินค้า")

if __name__ == "__main__":
    raw = input().strip()
    items = []
    if raw:
        for part in raw.split(";"):
            sku, quantity = part.split(",")
            items.append({"sku": sku, "quantity": int(quantity)})
    threshold = int(input())
    low = low_stock_skus(items, threshold)
    print(",".join(low) if low else "NONE")
