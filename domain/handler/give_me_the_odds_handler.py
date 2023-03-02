import networkx as nx

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from infrastructure.database.repository.implementation import route_repository


async def calculate_odds(request: GiveMeTheOddsRequest):
    routes = await route_repository.get_all_routes()
    print("routes from calculate_odds =", routes)

    number_of_planets = count_planets(routes, request.millennium_falcon.departure, request.millennium_falcon.arrival)
    print("number_of_planets of calculate_odds =", number_of_planets)
    return "Work in progress"


def count_planets(routes, origin, destination):
    graph = nx.DiGraph()
    for route in routes:
        graph.add_edge(route[0], route[1], weight=route[2])

    path = nx.shortest_path(graph, source=origin, target=destination, weight='weight')

    return len(path) - 2
