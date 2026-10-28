def prior_mean(values, index, window):
    # TODO: ใช้เฉพาะ slice ก่อน index
    raise NotImplementedError("เติมการเลือก window")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    index = int(input())
    window = int(input())
    result = prior_mean(values, index, window)
    print("NONE" if result is None else result)
