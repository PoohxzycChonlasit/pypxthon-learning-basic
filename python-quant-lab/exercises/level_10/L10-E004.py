def valid_bar(bar):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    import json
    bar = json.loads(input())
    # BUG: high >= low ไม่ได้ตรวจเทียบ open และ close
    valid = bar["high"] >= bar["low"] and bar["volume"] >= 0
    print(valid)
