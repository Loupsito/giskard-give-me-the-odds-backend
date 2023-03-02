from pydantic import BaseModel


class MillenniumFalcon(BaseModel):
    autonomy: int
    departure: str
    arrival: str
    routes_db: str
