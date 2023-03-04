import json

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from domain.handler.give_me_the_odds_handler import determine_odds_of_success
from domain.model.millennium_falcon import MillenniumFalcon
from infrastructure.database.database import DatabaseHandler
from infrastructure.database.repository import route_repository

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/give_me_the_odds")
async def give_me_the_odds(request: GiveMeTheOddsRequest):
    if request.millennium_falcon is None:
        with open('millennium-falcon.json', 'r') as file:
            request.millennium_falcon = MillenniumFalcon(**json.load(file))

    database_handler = await DatabaseHandler().get_database(request.millennium_falcon.routes_db)
    routes = await route_repository.get_all_routes(database_handler)

    return determine_odds_of_success(routes, request)
