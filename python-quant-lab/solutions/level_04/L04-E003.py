def compose_adjustment(amount, scale, offset):
    return amount * scale + offset

if __name__ == "__main__":
    amount = float(input())
    scale = float(input())
    offset = float(input())
    print(f"{compose_adjustment(amount, scale, offset):.1f}")
