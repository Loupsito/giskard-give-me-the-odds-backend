from typing import List

from pydantic import BaseModel

from domain.model.bounty_hunter import BountyHunter


class Empire(BaseModel):
    countdown: int
    bounty_hunters: List[BountyHunter]
