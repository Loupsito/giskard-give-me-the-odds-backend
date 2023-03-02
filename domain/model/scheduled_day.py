from pydantic import BaseModel


class ScheduledDay(BaseModel):
    planet: str
    day: int
