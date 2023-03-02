from typing import List

import networkx as nx

from infrastructure.database.repository.entity.route_entity import RouteEntity


def count_number_of_planet_stop(path: List[str]):
    return len(path) - 2


def determine_path(routes: [RouteEntity], origin: str, destination: str):
    graph = nx.DiGraph()
    for route in routes:
        graph.add_edge(route[0], route[1], weight=route[2])

    return nx.shortest_path(graph, source=origin, target=destination, weight='weight')


def calculate_total_time_travel(path: [str], routes: [RouteEntity]):
    total_time_travel = 0
    for i in range(0, len(path)):
        route = filter(lambda r: r.origin == path[i] and r.destination == path[i + 1], routes)
        for route_filtered in route:
            total_time_travel = total_time_travel + route_filtered.travel_time

    return total_time_travel
