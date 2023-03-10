from typing import List

import networkx as nx

from domain.model.empire import Empire
from infrastructure.database.entity.route_entity import RouteEntity


def get_ship_itinerary(routes: List[RouteEntity], origin: str, destination: str):
    graph = nx.DiGraph()
    for route in routes:
        graph.add_edge(route.origin, route.destination, weight=route.travel_time)

    return nx.shortest_path(graph, source=origin, target=destination, weight='weight')


def get_ship_total_travel_time(path: [str], routes: List[RouteEntity]):
    total_time_travel = 0

    if len(path) <= 1:
        raise ValueError("Path must have at least two nodes.")

    for i in range(0, len(path) - 1):
        origin = path[i]
        destination = path[i + 1]
        route_filter = filter(lambda r: r.origin == origin and r.destination == destination, routes)
        route = next(route_filter, None)
        if route is None:
            raise ValueError(f"No route found between {origin} and {destination}")
        total_time_travel += route.travel_time

    return total_time_travel


def get_num_potential_captures(path: [str], routes: List[RouteEntity], autonomy: int, empire: Empire):
    num_potential_capture = 0
    total_time_travel = 0
    initial_autonomy = autonomy

    for i in range(len(path) - 1):
        route = next((r for r in routes if r.origin == path[i] and r.destination == path[i + 1]), None)
        if route is None:
            continue

        total_time_travel += route.travel_time
        autonomy -= route.travel_time

        hunters_in_the_way = sum(1 for h in empire.bounty_hunters if h.day == total_time_travel)

        if autonomy <= 0 and hunters_in_the_way:
            num_potential_capture += 1
            autonomy = initial_autonomy

        elif hunters_in_the_way:
            num_potential_capture += hunters_in_the_way

    return num_potential_capture
