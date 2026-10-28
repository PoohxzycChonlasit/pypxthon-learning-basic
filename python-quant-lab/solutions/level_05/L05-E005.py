import csv
import io

def sales_report(lines):
    valid = 0
    rejected = 0
    revenue = 0.0
    for line in lines:
        try:
            row = next(csv.reader([line]))
            if len(row) != 2:
                raise ValueError
            quantity = int(row[0])
            price = float(row[1])
            if quantity < 0 or price < 0:
                raise ValueError
        except (csv.Error, StopIteration, ValueError):
            rejected += 1
            continue
        valid += 1
        revenue += quantity * price
    return {"valid": valid, "rejected": rejected, "revenue": revenue}

if __name__ == "__main__":
    import sys
    report = sales_report(sys.stdin.read().splitlines())
    print(f"valid={report['valid']} rejected={report['rejected']} revenue={report['revenue']:.2f}")
