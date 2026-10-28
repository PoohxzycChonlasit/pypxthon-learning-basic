def revenue_by_product(rows):
    raise NotImplementedError("TODO: รวมรายได้ตาม product")

if __name__ == "__main__":
    import csv
    import sys
    rows = list(csv.DictReader(sys.stdin))
    report = revenue_by_product(rows)
    if not report:
        print("NONE")
    else:
        for product in sorted(report):
            print(f"{product}:{report[product]:.2f}")
