from pydantic import BaseModel


class Route(BaseModel):
    origin: str
    description: str
    travel_time: int

    class Config:
        orm_mode = True
