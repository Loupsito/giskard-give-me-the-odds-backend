from fastapi import FastAPI

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.handler.give_me_the_odds_handler import determine_odds
from domain.model.odds import Odds
from infrastructure.database.database import database_engine

app = FastAPI()


@app.on_event("startup")
async def database_connect():
    await database_engine.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database_engine.disconnect()


@app.post("/give_me_the_odds")
async def give_me_the_odds(request: GiveMeTheOddsRequest):
    return await determine_odds(request)
