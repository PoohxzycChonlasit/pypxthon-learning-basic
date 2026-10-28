def sum_at_or_below_limit(values, limit):
    total = 0
    for value in values:
        if value <= limit:
            total += value
    return total

if __name__ == "__main__":
    limit = int(input())
    values = [int(value) for value in input().split()]
    print(sum_at_or_below_limit(values, limit))
