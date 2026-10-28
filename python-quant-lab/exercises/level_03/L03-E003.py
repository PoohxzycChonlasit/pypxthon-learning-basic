def frequency_table(tags):
    # TODO: คืน dict ที่ map tag ไปยังจำนวนครั้ง
    raise NotImplementedError("เติมตัวนับ")

if __name__ == "__main__":
    raw = input().strip()
    tags = raw.split(",") if raw else []
    print(sorted(frequency_table(tags).items()))
