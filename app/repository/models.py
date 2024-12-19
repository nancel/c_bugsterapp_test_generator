from app.repository.database import Base
from sqlalchemy import Column, Integer, String, JSON


class EventModel(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, index=True)
    properties = Column(JSON)
    timestamp = Column(String)
