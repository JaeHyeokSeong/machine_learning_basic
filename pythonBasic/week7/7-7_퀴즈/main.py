print("7-7_퀴즈\n")


def std_weight(height: float, gender: str) -> None:
    height /= 100  # change cm -> m
    weight = height * height
    if gender == "m":
        weight *= 22
    elif gender == "f":
        weight *= 21
    print(f"{weight:.2f}")


std_weight(175, "m")
