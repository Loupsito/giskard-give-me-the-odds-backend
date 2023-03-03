import networkx as nx

from domain.model.empire import Empire
from infrastructure.database.repository.entity.route_entity import RouteEntity


def count_number_of_planet_stop(path: [str]):
    return len(path) - 2


def get_path(routes: [RouteEntity], origin: str, destination: str):
    graph = nx.DiGraph()
    for route in routes:
        graph.add_edge(route[0], route[1], weight=route[2])

    return nx.shortest_path(graph, source=origin, target=destination, weight='weight')


def get_total_time_travel(path: [str], routes: [RouteEntity]):
    total_time_travel = 0
    for i in range(0, len(path)):
        route = filter(lambda r: r.origin == path[i] and r.destination == path[i + 1], routes)
        for route_filtered in route:
            total_time_travel = total_time_travel + route_filtered.travel_time

    return total_time_travel


def get_number_of_potential_capture(path: [str], routes: [RouteEntity], autonomy: int, empire: Empire):
    num_potential_capture = 0
    total_time_travel = 0
    initial_autonomy = autonomy

    for i in range(len(path) - 1):
        route = next((r for r in routes if r.origin == path[i] and r.destination == path[i + 1]), None)
        if route is None:
            continue

        total_time_travel += route.travel_time
        autonomy -= route.travel_time

        if autonomy <= 0:
            num_potential_capture += 1
            autonomy = initial_autonomy

        if i < len(path) - 2:
            hunters_in_the_way = sum(1 for h in empire.bounty_hunters if h.day == total_time_travel)
            num_potential_capture += hunters_in_the_way

    return num_potential_capture
