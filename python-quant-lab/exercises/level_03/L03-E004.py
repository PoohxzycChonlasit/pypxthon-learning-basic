def unique_in_order(items):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    items = input().split(",")
    # BUG: sorting removes duplicates but changes first-seen order
    print(sorted(set(items)))
