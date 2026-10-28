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
