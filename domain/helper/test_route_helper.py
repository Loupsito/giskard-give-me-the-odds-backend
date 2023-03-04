import networkx as nx
import pytest

from domain.helper.route_helper import get_ship_itinerary, get_ship_total_travel_time, get_num_potential_captures
from domain.model.bounty_hunter import BountyHunter
from domain.model.empire import Empire
from infrastructure.database.entity.route_entity import RouteEntity


def test_get_ship_itinerary_returns_correct_itinerary():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('A', 'C', 30),
        RouteEntity('B', 'D', 50),
        RouteEntity('D', 'C', 30),
        RouteEntity('B', 'E', 100),
        RouteEntity('E', 'C', 10)
    ]

    expected_itinerary = ['A', 'B', 'C']

    assert get_ship_itinerary(routes, 'A', 'C') == expected_itinerary


def test_get_ship_itinerary_raises_exception_if_origin_or_destination_not_in_graph():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('B', 'D', 30),
    ]

    with pytest.raises(nx.NodeNotFound):
        get_ship_itinerary(routes, 'X', 'C')
        get_ship_itinerary(routes, 'A', 'Y')


def test_get_ship_itinerary_raises_exception_if_no_route_found():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('B', 'D', 50),
    ]

    with pytest.raises(nx.NetworkXNoPath):
        get_ship_itinerary(routes, 'A', 'D')
        get_ship_itinerary(routes, 'B', 'A')


def test_get_ship_total_travel_time_returns_correct_total_travel_time():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('A', 'C', 30),
        RouteEntity('B', 'D', 50),
        RouteEntity('D', 'C', 30),
        RouteEntity('B', 'E', 100),
        RouteEntity('E', 'C', 10)
    ]
    path = ['A', 'B', 'C']
    expected_total_travel_time = 25

    assert get_ship_total_travel_time(path, routes) == expected_total_travel_time


def test_get_ship_total_travel_time_raises_exception_if_path_not_provided():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('A', 'C', 30)
    ]

    with pytest.raises(TypeError):
        get_ship_total_travel_time(None, routes)


def test_get_ship_total_travel_time_raises_exception_if_path_has_only_one_location():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('A', 'C', 30)
    ]
    path = ['A']

    with pytest.raises(ValueError):
        get_ship_total_travel_time(path, routes)


def test_get_ship_total_travel_time_raises_exception_if_route_not_found():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('A', 'C', 30)
    ]
    path = ['A', 'Z']

    with pytest.raises(ValueError):
        get_ship_total_travel_time(path, routes)


def test_get_num_potential_captures_returns_correct_num():
    routes = [
        RouteEntity('A', 'B', 6),
        RouteEntity('B', 'C', 1),
        RouteEntity('C', 'D', 1)
    ]
    empire = Empire(
        countdown=3,
        bounty_hunters=[
            BountyHunter(planet='B', day=6),
            BountyHunter(planet='B', day=7),
            BountyHunter(planet='D', day=8)
        ]
    )
    path = ['A', 'B', 'C']
    autonomy = 6
    expected_num = 2

    assert get_num_potential_captures(path, routes, autonomy, empire) == expected_num


def test_get_num_potential_captures_handles_no_hunters():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('C', 'D', 20)
    ]
    empire = Empire(countdown=3, bounty_hunters=[])
    path = ['A', 'B', 'C', 'D']
    autonomy = 50
    expected_num = 0

    assert get_num_potential_captures(path, routes, autonomy, empire) == expected_num


def test_get_num_potential_captures_handles_zero_autonomy():
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('C', 'D', 20)
    ]
    empire = Empire(countdown=3, bounty_hunters=[])
    path = ['A', 'B', 'C', 'D']
    autonomy = 0
    expected_num = 0

    assert get_num_potential_captures(path, routes, autonomy, empire) == expected_num
