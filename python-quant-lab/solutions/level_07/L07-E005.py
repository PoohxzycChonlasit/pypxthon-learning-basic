def compare_campaigns(a_signups, a_visits, b_signups, b_visits):
    if a_visits == 0 or b_visits == 0:
        return None
    a_rate = a_signups / a_visits
    b_rate = b_signups / b_visits
    if a_rate > b_rate:
        winner = "A"
    elif b_rate > a_rate:
        winner = "B"
    else:
        winner = "tie"
    return {"a_rate": a_rate, "b_rate": b_rate, "winner": winner}

if __name__ == "__main__":
    a_signups, a_visits, b_signups, b_visits = [float(input()) for _ in range(4)]
    result = compare_campaigns(a_signups, a_visits, b_signups, b_visits)
    if result is None:
        print("INVALID")
    else:
        print(f"A={result['a_rate']:.2f} B={result['b_rate']:.2f} winner={result['winner']}")
