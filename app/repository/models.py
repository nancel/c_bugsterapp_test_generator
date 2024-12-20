from app.repository.database import Base
from sqlalchemy import Column, Integer, String, JSON


class EventModel(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, index=True)
    distinct_id = Column(String)
    session_id = Column(String)
    journey_id = Column(String)
    current_url = Column(String)
    host = Column(String)
    pathname = Column(String)
    browser = Column(String)
    device = Column(String)
    event_type = Column(String)
    element_type = Column(String)
    element_text = Column(String)
    element_attributes = Column(JSON)
    timestamp = Column(String)
