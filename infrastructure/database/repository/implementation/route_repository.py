from sqlalchemy.orm import Session

from ... import models


def get_route(db: Session, origin: str, destination: str):
    return db.query(models.Route).filter(
        models.Route.origin == origin and models.Route.destination == destination).first()


def get_all_routes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Route).all()
