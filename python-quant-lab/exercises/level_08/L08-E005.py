def exposure_report(equity, positions, max_fraction):
    raise NotImplementedError("TODO: ตรวจและรวม exposure")

if __name__ == "__main__":
    import json
    equity = float(input())
    positions = json.loads(input())
    max_fraction = float(input())
    report = exposure_report(equity, positions, max_fraction)
    if report is None:
        print("INVALID")
    else:
        limit = equity * max_fraction
        print(f"exposure={report['exposure']:.2f} limit={limit:.2f} allowed={report['allowed']}")
