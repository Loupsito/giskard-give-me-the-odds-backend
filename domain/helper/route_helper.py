import networkx as nx

from domain.model.empire import Empire
from infrastructure.database.repository.entity.route_entity import RouteEntity


def count_number_of_planet_stop(path: [str]):
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


def get_number_of_potential_capture(path: [str], routes: [RouteEntity], autonomy: int, empire: Empire):
    new_autonomy = autonomy
    number_of_potential_capture = 0
    total_time_travel = 0
    print("first = ", path[0], " ==> last = ", path[-1])
    for i in range(0, len(path)):
        route = filter(lambda r: r.origin == path[i] and r.destination == path[i + 1], routes)
        for route_filtered in route:
            new_autonomy = new_autonomy - route_filtered.travel_time
            total_time_travel = total_time_travel + route_filtered.travel_time

        if new_autonomy <= 0:
            print("no more autonomy !")
            number_of_potential_capture += 1
            new_autonomy = autonomy

        if path[i] != path[len(path)-2] and path[i] != path[-1]:
            hunters_in_the_way: int = len(list(filter(lambda hunter: hunter.day == total_time_travel, empire.bounty_hunters)))
            number_of_potential_capture += hunters_in_the_way

    return number_of_potential_capture
