def prior_mean(values, index, window):
    if window <= 0 or index < window or index >= len(values):
        return None
    previous = values[index - window:index]
    return sum(previous) / window

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    result = prior_mean(values, index, window)
    print("NONE" if result is None else result)
