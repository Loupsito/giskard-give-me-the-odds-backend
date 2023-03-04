from pydantic import BaseModel


class MillenniumFalcon(BaseModel):
    autonomy: int
    departure: str
    arrival: str
    routes_db: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
