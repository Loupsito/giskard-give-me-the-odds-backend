from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.helper.probability_helper import get_prob_captured, calculate_odds
from domain.helper.route_helper import get_ship_total_travel_time, get_ship_itinerary, \
    get_num_potential_captures
from domain.model.odds import Odds
from infrastructure.database.entity.route_entity import RouteEntity


def determine_odds_of_success(routes: [RouteEntity], request: GiveMeTheOddsRequest) -> Odds:
    ship_itinerary = get_ship_itinerary(routes, request.millennium_falcon.departure, request.millennium_falcon.arrival)
    ship_total_travel_time = get_ship_total_travel_time(ship_itinerary, routes)
    num_potential_captures = get_num_potential_captures(ship_itinerary, routes, request.millennium_falcon.autonomy,
                                                        request.empire)
    prob_captured = get_prob_captured(num_potential_captures)
    odds_of_success = calculate_odds(prob_captured, ship_total_travel_time, request.empire.countdown)
    return Odds(odds_of_success)
