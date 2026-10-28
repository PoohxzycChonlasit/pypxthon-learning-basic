def fill_forward(values):
    result = []
    previous = None
    for value in values:
        if value is not None:
            previous = value
            result.append(value)
        else:
            result.append(previous)
    return result

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [None if x == "NA" else float(x) for x in raw.split(",")]
    print(fill_forward(values))
