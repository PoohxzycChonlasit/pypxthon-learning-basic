def exposure_report(equity, positions, max_fraction):
    if equity <= 0 or not 0 <= max_fraction <= 1:
        return None
    if any(value < 0 for value in positions.values()):
        return None
    exposure = sum(positions.values())
    return {"exposure": exposure, "allowed": exposure <= equity * max_fraction}

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
