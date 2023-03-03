from typing import Any

from pydantic import BaseModel


class BountyHunter(BaseModel):
    planet: str
    day: int
