def get_prob_captured(number_of_planets: int):
    if number_of_planets < 0:
        raise ValueError("The number of planet must be at least 1")
    result = 0.0
    for i in range(number_of_planets):
        result += (9.0 ** i) / (10.0 ** (i + 1))
    return result


def calculate_odds(probability_of_being_captured: float, countdown: int, total_time_travel: int):
    if probability_of_being_captured < 0 or probability_of_being_captured > 1:
        raise ValueError("The probability of being captured must be between 0 and 1")
    if total_time_travel <= countdown:
        return 0
    return 100 - (100 * probability_of_being_captured)
