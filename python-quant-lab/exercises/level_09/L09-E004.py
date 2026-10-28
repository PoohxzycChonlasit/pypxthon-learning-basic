def trailing_mean(values, index, window):
    raise NotImplementedError("ดู look-ahead ใน main")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    # BUG: รวมค่าปัจจุบันและหารด้วย window + 1
    section = values[index - window:index + 1]
    print(sum(section) / len(section) if len(section) == window + 1 else "NONE")
