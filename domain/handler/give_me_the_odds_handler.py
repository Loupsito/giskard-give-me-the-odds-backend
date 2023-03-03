from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.helper.probability_helper import get_prob_captured, calculate_odds
from domain.helper.route_helper import get_ship_total_travel_time, get_ship_itinerary, \
    get_num_potential_captures
from domain.model.odds import Odds
from infrastructure.database.repository import route_repository


async def determine_odds_of_success(request: GiveMeTheOddsRequest) -> Odds:
    routes = await route_repository.get_all_routes()
    ship_itinerary = get_ship_itinerary(routes, request.millennium_falcon.departure, request.millennium_falcon.arrival)
    ship_total_travel_time = get_ship_total_travel_time(ship_itinerary, routes)
    number_of_potential_capture = get_num_potential_captures(ship_itinerary, routes, request.millennium_falcon.autonomy,
                                                             request.empire)
    prob_captured = get_prob_captured(number_of_potential_capture)
    odds_of_success = calculate_odds(prob_captured, ship_total_travel_time, request.empire.countdown)
    return Odds(odds_of_success)
