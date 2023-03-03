from unittest.mock import AsyncMock

import pytest

from infrastructure.database.repository.route_repository import get_all_routes


@pytest.fixture
def database_engine_mock():
    return AsyncMock()


@pytest.mark.asyncio
async def test_get_all_routes(database_engine_mock):
    # Set up the mock database engine to return some test data
    test_data = [(1, 'Tatooine', 'Dagobah', 6), (2, 'Dagobah', 'Endor', 4)]
    database_engine_mock.fetch_all.return_value = test_data

    # Call the function and get the result
    result = await get_all_routes()

    # Assert that the mock method was called with the expected query
    database_engine_mock.fetch_all.assert_called_once_with(query="SELECT * from routes")

    # Assert that the function returned the expected data
    assert result == test_data
