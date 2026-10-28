def revenue_by_product(rows):
    totals = {}
    for row in rows:
        product = row["product"]
        revenue = float(row["quantity"]) * float(row["unit_price"])
        totals[product] = totals.get(product, 0.0) + revenue
    return totals

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
