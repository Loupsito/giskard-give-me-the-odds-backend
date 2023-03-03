from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.helper.probability_helper import get_probability_of_being_captured, calculate_odds
from domain.helper.route_helper import get_total_time_travel, count_number_of_planet_stop, get_path, \
    get_number_of_potential_capture
from domain.model.odds import Odds
from infrastructure.database.repository.entity.route_entity import RouteEntity
from infrastructure.database.repository.implementation import route_repository


async def determine_odds(request: GiveMeTheOddsRequest):
    routes: [RouteEntity] = await route_repository.get_all_routes()
    print("routes from calculate_odds =", routes)

    path: [str] = get_path(routes, request.millennium_falcon.departure, request.millennium_falcon.arrival)
    print("path ==> ", path)

    number_of_planet_stop: int = count_number_of_planet_stop(path)
    print("number_of_planets =", number_of_planet_stop)

    total_time_travel: int = get_total_time_travel(path, routes)
    print("total_time_travel ==> ", total_time_travel)

    number_of_potential_capture: int = get_number_of_potential_capture(path, routes, request.millennium_falcon.autonomy,
                                                                       request.empire)
    print("number_of_potential_capture ==> ", number_of_potential_capture)

    probability_of_being_captured: float = get_probability_of_being_captured(number_of_potential_capture)
    print("probability_of_being_captured =", probability_of_being_captured)

    odds = Odds(calculate_odds(probability_of_being_captured, total_time_travel, request.empire.countdown))
    print("odds =", odds.value, "%")
    return odds
