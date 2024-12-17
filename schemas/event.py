from pydantic import BaseModel
from typing import Optional, Dict


class EventProperties(BaseModel):
    distinct_id: str
    session_id: str
    journey_id: str
    current_url: str
    host: str
    pathname: str
    browser: str
    device: str
    event_type: str
    element_type: Optional[str] = None
    element_text: Optional[str] = None
    element_attributes: Optional[Dict[str, str]] = None


class Event(BaseModel):
    event: str
    properties: EventProperties
    timestamp: str
