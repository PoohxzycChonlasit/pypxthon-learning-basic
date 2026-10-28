def conversion_rate(signups, visits):
    raise NotImplementedError("ดูบั๊กใน main")

if __name__ == "__main__":
    signups = float(input())
    visits = float(input())
    # BUG: เศษส่วนกลับด้านและตรวจตัวตั้ง
    rate = None if signups == 0 else visits / signups
    print("NONE" if rate is None else rate)
