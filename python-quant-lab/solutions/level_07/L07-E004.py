def conversion_rate(signups, visits):
    if visits == 0:
        return None
    return signups / visits

if __name__ == "__main__":
    signups = float(input())
    visits = float(input())
    rate = conversion_rate(signups, visits)
    print("NONE" if rate is None else rate)
