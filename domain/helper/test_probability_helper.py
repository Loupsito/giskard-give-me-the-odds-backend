from math import isclose

import pytest

from domain.helper.probability_helper import get_prob_captured, calculate_odds


def test_get_prob_captured_with_one_planet():
    assert isclose(get_prob_captured(1), 0.1)


def test_get_prob_captured_with_two_planets():
    assert isclose(get_prob_captured(2), 0.19)


def test_get_prob_captured_with_three_planets():
    assert isclose(get_prob_captured(3), 0.271)


def test_get_prob_captured_with_zero_planets():
    assert get_prob_captured(0) == 0.0


def test_get_prob_captured_with_negative_number_of_planets():
    with pytest.raises(ValueError):
        get_prob_captured(-1)


def test_calculate_odds_returns_zero_if_total_time_travel_less_than_or_equal_to_countdown():
    assert calculate_odds(0.9, 10, 10) == 0
    assert calculate_odds(0.5, 5, 5) == 0
    assert calculate_odds(0.2, 0, 0) == 0


def test_calculate_odds_returns_correct_value_if_total_time_travel_greater_than_countdown():
    assert calculate_odds(0.9, 10, 20) == 10
    assert calculate_odds(0.5, 5, 10) == 50
    assert calculate_odds(0.2, 0, 100) == 80


def test_calculate_odds_raises_exception_if_probability_of_being_captured_is_greater_than_one():
    with pytest.raises(ValueError):
        calculate_odds(1.5, 10, 20)
        calculate_odds(2, 5, 10)
        calculate_odds(10, 0, 100)


def test_calculate_odds_raises_exception_if_probability_of_being_captured_is_less_than_zero():
    with pytest.raises(ValueError):
        calculate_odds(-0.5, 10, 20)
        calculate_odds(-1, 5, 10)
        calculate_odds(-10, 0, 100)
