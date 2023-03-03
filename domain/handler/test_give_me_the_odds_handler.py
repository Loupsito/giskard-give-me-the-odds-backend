import pytest

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.handler.give_me_the_odds_handler import determine_odds_of_success
from domain.model.bounty_hunter import BountyHunter
from domain.model.empire import Empire
from domain.model.millennium_falcon import MillenniumFalcon
from infrastructure.database.entity.route_entity import RouteEntity


@pytest.mark.asyncio
async def test_determine_odds_of_success(mocker):
    routes = [
        RouteEntity('A', 'B', 10),
        RouteEntity('B', 'C', 15),
        RouteEntity('C', 'D', 20)
    ]

    # Mock the sqlite3.connect() function
    mock_connect = mocker.patch('sqlite3.connect')

    # Mock the cursor.execute() and cursor.fetchall() methods
    mock_cursor = mock_connect.return_value.cursor.return_value
    mock_cursor.execute.return_value.fetchall.return_value = routes

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

    expected_num = 81.0

    await determine_odds_of_success(request)
