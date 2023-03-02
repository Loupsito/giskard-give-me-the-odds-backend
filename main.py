import logging

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from domain.dto.give_me_the_odds_request import GiveMeTheOddsRequest
from infrastructure.database import models
from infrastructure.database.database import engine, get_db
from infrastructure.database.repository.implementation import route_repository

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/give_me_the_odds")
def give_me_the_odds(request: GiveMeTheOddsRequest, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # time_travel = route_repository.get_travel_time(db, request.millennium_falcon.departure,
    #                                              request.millennium_falcon.arrival)
    routes = route_repository.get_all_routes(db, skip=skip, limit=limit)
    print("request =", request)
    print("routes =", routes)
    return routes
