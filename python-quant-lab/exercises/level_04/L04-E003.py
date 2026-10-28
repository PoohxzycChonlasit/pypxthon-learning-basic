def compose_adjustment(amount, scale, offset):
    # TODO: คืน amount * scale + offset
    raise NotImplementedError("เติมสูตร")

if __name__ == "__main__":
    amount = float(input())
    scale = float(input())
    offset = float(input())
    print(f"{compose_adjustment(amount, scale, offset):.1f}")
