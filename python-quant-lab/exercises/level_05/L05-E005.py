def sales_report(lines):
    raise NotImplementedError("TODO: parse, validate, and total rows")

if __name__ == "__main__":
    import sys
    report = sales_report(sys.stdin.read().splitlines())
    print(f"valid={report['valid']} rejected={report['rejected']} revenue={report['revenue']:.2f}")
