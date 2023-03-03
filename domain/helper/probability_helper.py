def get_prob_captured(number_of_planets: int):
    result = 0.0
    for i in range(number_of_planets):
        result += (9.0 ** i) / (10.0 ** (i + 1))
    return result


def calculate_odds(probability_of_being_captured: float, countdown: int, total_time_travel: int):
    if total_time_travel <= countdown:
        return 0
    return 100 - (100 * probability_of_being_captured)
