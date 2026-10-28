def population_variance(values):
    if not values:
        return None
    mean = sum(values) / len(values)
    squared = [(value - mean) ** 2 for value in values]
    return sum(squared) / len(values)

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    result = population_variance(values)
    print("NONE" if result is None else result)
