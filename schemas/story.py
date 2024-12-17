from pydantic import BaseModel
from typing import List
from schemas.event import Event


class Story(BaseModel):
    name: str = ''
    actions: List[Event] = []
