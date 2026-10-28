def exposure_fraction(price, quantity, equity):
    return price * quantity / equity if equity else None
