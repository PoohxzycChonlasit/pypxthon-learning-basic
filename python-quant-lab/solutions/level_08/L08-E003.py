def risk_based_quantity(equity, risk_percent, stop_distance):
    if equity <= 0 or risk_percent < 0 or stop_distance <= 0:
        return 0
    risk_budget = equity * risk_percent / 100
    return risk_budget / stop_distance

if __name__ == "__main__":
    equity = float(input())
    risk_percent = float(input())
    stop_distance = float(input())
    print(f"{risk_based_quantity(equity, risk_percent, stop_distance):.2f}")
