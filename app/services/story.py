from sqlalchemy.orm import Session
from app.repository.crud import get_events
from app.processors.event_processor import EventProcessor


class StoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_stories(self, session_id=None):
        events = get_events(self.db, session_id)

        processor = EventProcessor()
        for event in events:
            processor.add_event(event)

        return processor.generate_stories()
