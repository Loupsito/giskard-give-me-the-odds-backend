from app_module import app
from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.handler.give_me_the_odds_handler import determine_odds


@app.post("/give_me_the_odds")
async def give_me_the_odds(request: GiveMeTheOddsRequest):
    result = await determine_odds(request)
    print("request =", request)
    print("routes =", result)
    return request
