from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_give_me_the_odds():
    response = client.post(
        "/give_me_the_odds",
        json={
            "millennium_falcon": {
                "autonomy": 6,
                "departure": "Tatooine",
                "arrival": "Endor",
                "routes_db": "universe.db"
            },
            "empire": {
                "countdown": 8,
                "bounty_hunters": [
                    {
                        "planet": "Hoth",
                        "day": 6
                    },
                    {
                        "planet": "Hoth",
                        "day": 7
                    },
                    {
                        "planet": "Hoth",
                        "day": 8
                    }
                ]
            }
        },
    )
    assert response.status_code == 200
    assert response.text == '{"value":81.0}'


def test_give_me_the_odds_with_countdown_too_short():
    response = client.post(
        "/give_me_the_odds",
        json={
            "millennium_falcon": {
                "autonomy": 6,
                "departure": "Tatooine",
                "arrival": "Endor",
                "routes_db": "universe.db"
            },
            "empire": {
                "countdown": 7,
                "bounty_hunters": [
                    {
                        "planet": "Hoth",
                        "day": 6
                    },
                    {
                        "planet": "Hoth",
                        "day": 7
                    },
                    {
                        "planet": "Hoth",
                        "day": 8
                    }
                ]
            }
        },
    )
    assert response.status_code == 200
    assert response.text == '{"value":0}'
