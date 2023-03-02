from sqlalchemy import Column, String, Integer

from .database import Base


class Route(Base):
    __tablename__ = "routes"

    origin = Column(String, primary_key=True, index=True)
    destination = Column(String)
    travel_time = Column(Integer)
