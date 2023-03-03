import pytest
import networkx as nx

from domain.helper.route_helper import get_ship_itinerary, get_ship_total_travel_time
from infrastructure.database.entity.route_entity import RouteEntity


def test_get_ship_itinerary_returns_correct_itinerary():
    routes = [
        ('A', 'B', 10),
        ('B', 'C', 15),
        ('A', 'C', 30),
        ('B', 'D', 50),
        ('D', 'C', 30),
        ('B', 'E', 100),
        ('E', 'C', 10)
    ]
    expected_itinerary = ['A', 'B', 'C']

    assert get_ship_itinerary(routes, 'A', 'C') == expected_itinerary


def test_get_ship_itinerary_raises_exception_if_origin_or_destination_not_in_graph():
    routes = [
        ('A', 'B', 10),
        ('B', 'C', 15),
        ('B', 'D', 50)
    ]

    with pytest.raises(nx.NodeNotFound):
        get_ship_itinerary(routes, 'X', 'C')
        get_ship_itinerary(routes, 'A', 'Y')


def test_get_ship_itinerary_raises_exception_if_no_route_found():
    routes = [
        ('A', 'B', 10),
        ('B', 'C', 15),
        ('B', 'D', 50)
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


