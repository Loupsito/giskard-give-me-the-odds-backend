from typing import Union

from pydantic import BaseModel

from domain.model.empire import Empire
from domain.model.millennium_falcon import MillenniumFalcon


class GiveMeTheOddsRequest(BaseModel):
    millennium_falcon: Union[MillenniumFalcon, None] = None
    empire: Empire
