def calculate_probability_of_being_captured(number_of_planets: int):
    result = 0.0
    for i in range(number_of_planets):
        result += (9.0 ** i) / (10.0 ** (i + 1))
    return result
