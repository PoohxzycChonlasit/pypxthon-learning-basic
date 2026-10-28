def rolling_means(values, window):
    if window <= 0 or len(values) < window:
        return []
    result = []
    for start in range(len(values) - window + 1):
        section = values[start:start + window]
        result.append(sum(section) / window)
    return result

if __name__ == "__main__":
    values = [float(value) for value in input().split()]
    window = int(input())
    print(rolling_means(values, window))
