from pydantic import BaseModel
from typing import List


class Action(BaseModel):
    type: str
    target: str = ''
    value: str = ''
    url: str = ''
    pathname: str = ''
    element_text: str = ''


class Story(BaseModel):
    name: str = ''
    actions: List[Action] = []
