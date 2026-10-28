def compare_campaigns(a_signups, a_visits, b_signups, b_visits):
    raise NotImplementedError("TODO: คำนวณ rates และเลือกผู้ชนะ")

if __name__ == "__main__":
    a_signups, a_visits, b_signups, b_visits = [float(input()) for _ in range(4)]
    result = compare_campaigns(a_signups, a_visits, b_signups, b_visits)
    if result is None:
        print("INVALID")
    else:
        print(f"A={result['a_rate']:.2f} B={result['b_rate']:.2f} winner={result['winner']}")
