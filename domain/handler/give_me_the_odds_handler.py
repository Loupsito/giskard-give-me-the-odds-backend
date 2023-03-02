from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.helper.odds_helper import calculate_probability_of_being_captured
from domain.helper.route_helper import calculate_total_time_travel, count_number_of_planet_stop, determine_path
from infrastructure.database.repository.entity.route_entity import RouteEntity
from infrastructure.database.repository.implementation import route_repository


async def determine_odds(request: GiveMeTheOddsRequest):
    routes: [RouteEntity] = await route_repository.get_all_routes()
    print("routes from calculate_odds =", routes)

    path: [str] = determine_path(routes, request.millennium_falcon.departure, request.millennium_falcon.arrival)
    print("path ==> ", path)

    number_of_planet_stop: int = count_number_of_planet_stop(path)
    print("number_of_planets =", number_of_planet_stop)

    total_time_travel: int = calculate_total_time_travel(path, routes)
    print("total_time_travel ==> ", total_time_travel)

    odds: float = calculate_probability_of_being_captured(number_of_planet_stop)
    print("calculate_odds =", odds)
    return "Work in progress"
