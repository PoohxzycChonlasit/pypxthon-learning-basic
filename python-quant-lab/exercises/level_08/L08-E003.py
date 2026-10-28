def risk_based_quantity(equity, risk_percent, stop_distance):
    # TODO: ตรวจค่าก่อนหารและคืนขนาดหน่วย
    raise NotImplementedError("เติมสูตร position sizing")

if __name__ == "__main__":
    equity = float(input())
    risk_percent = float(input())
    stop_distance = float(input())
    print(f"{risk_based_quantity(equity, risk_percent, stop_distance):.2f}")
