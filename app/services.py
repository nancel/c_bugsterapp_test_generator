from sqlalchemy.orm import Session
from app.crud import create_event, get_events
from app.processors.event_processor import EventProcessor
from app.processors.story_processor import StoryProcessor


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


class StoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_stories(self, session_id=None):
        events = get_events(self.db, session_id)

        processor = EventProcessor()
        for event in events:
            processor.add_event(event)

        return processor.generate_stories()


class TestService:
    def __init__(self, db: Session):
        self.db = db

    def get_tests(self, session_id=None):
        story_service = StoryService(self.db)
        stories = story_service.get_stories(session_id)

        story_processor = StoryProcessor()
        for story in stories:
            story_processor.add_story(story)

        return story_processor.generate_tests()
