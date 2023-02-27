from typing import List

from pydantic import BaseModel

from domain.models.scheduled_day import ScheduledDay


class Empire(BaseModel):
    countdown: int
    bounty_hunters: List[ScheduledDay]
