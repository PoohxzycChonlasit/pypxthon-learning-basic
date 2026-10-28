def population_variance(values):
    # TODO: mean แล้วหาค่าเฉลี่ย squared deviations
    raise NotImplementedError("เติมสูตร variance")

if __name__ == "__main__":
    raw = input().strip()
    values = [] if not raw else [float(value) for value in raw.split(",")]
    result = population_variance(values)
    print("NONE" if result is None else result)
