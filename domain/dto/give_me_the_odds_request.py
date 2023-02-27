from typing import Union

from pydantic import BaseModel

from domain.models.empire import Empire
from domain.models.millennium_falcon import MillenniumFalcon


class GiveMeTheOddsRequest(BaseModel):
    millennium_falcon: Union[MillenniumFalcon, None] = None
    empire: Empire
