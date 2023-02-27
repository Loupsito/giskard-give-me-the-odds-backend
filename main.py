from fastapi import FastAPI

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest

app = FastAPI()


@app.post("/give_me_the_odds")
def concatenate_strings(request: GiveMeTheOddsRequest):
    print("request =", request)
    return request
