def frequency_table(tags):
    counts = {}
    for tag in tags:
        counts[tag] = counts.get(tag, 0) + 1
    return counts

if __name__ == "__main__":
    raw = input().strip()
    tags = raw.split(",") if raw else []
    print(sorted(frequency_table(tags).items()))
