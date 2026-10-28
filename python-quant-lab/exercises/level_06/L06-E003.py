def rolling_means(values, window):
    # TODO: คืนค่าเฉลี่ยของแต่ละ slice ที่ยาว window
    raise NotImplementedError("เติม rolling window")

if __name__ == "__main__":
    values = [float(value) for value in input().split()]
    window = int(input())
    print(rolling_means(values, window))
