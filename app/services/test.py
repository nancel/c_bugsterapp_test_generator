from sqlalchemy.orm import Session
from app.processors.story_processor import StoryProcessor
from app.services.story import StoryService


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
