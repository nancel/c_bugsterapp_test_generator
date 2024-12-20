from sqlalchemy.orm import Session
from app.repository.crud import create_event, get_events


class EventService:
    def __init__(self, db: Session):
        self.db = db

    def create_events(self, events):
        created_events = []

        for event in events:
            event = create_event(self.db, event)
            created_events.append(event)

        return created_events

    def get_events(self, session_id=None):
        return get_events(self.db, session_id)
