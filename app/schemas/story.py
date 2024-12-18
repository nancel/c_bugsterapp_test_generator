from pydantic import BaseModel
from typing import List
from app.schemas.event import Event


class Story(BaseModel):
    name: str = ''
    actions: List[Event] = []
