def csv_field_count(line):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    line = input()
    # BUG: comma ใน quoted field ไม่ใช่ตัวแบ่งคอลัมน์
    print(len(line.split(",")))
