from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.handler.give_me_the_odds_handler import determine_odds_of_success
from domain.model.bounty_hunter import BountyHunter
from domain.model.empire import Empire
from domain.model.millennium_falcon import MillenniumFalcon
from infrastructure.database.entity.route_entity import RouteEntity


def test_determine_odds_of_success():
    routes = [
        RouteEntity('Tatooine', 'Dagobah', 6),
        RouteEntity('Dagobah', 'Endor', 4),
        RouteEntity('Dagobah', 'Hoth', 1),
        RouteEntity('Hoth', 'Endor', 1),
        RouteEntity('Tatooine', 'Hoth', 6),
    ]

    # create a MillenniumFalcon object
    millennium_falcon = MillenniumFalcon(
        autonomy=6,
        departure='Tatooine',
        arrival='Endor',
        routes_db='routes.db'
    )

    # create a list of BountyHunter objects
    bounty_hunters = [
        BountyHunter(planet='Hoth', day=6),
        BountyHunter(planet='Hoth', day=7),
        BountyHunter(planet='Hoth', day=8)
    ]

    # create an Empire object
    empire = Empire(
        countdown=8,
        bounty_hunters=bounty_hunters
    )

    # create a GiveMeTheOddsRequest object
    request = GiveMeTheOddsRequest(
        millennium_falcon=millennium_falcon,
        empire=empire
    )

    expected_odds = 81.0

    assert determine_odds_of_success(routes, request).value == expected_odds
