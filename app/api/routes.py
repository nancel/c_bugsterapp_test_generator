from typing import Optional, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.event import Event
from app.schemas.story import Story
from app.schemas.test import Test
from app.services import EventService, StoryService, TestService

router = APIRouter()


@router.post("/api/events", summary="Crear eventos", tags=["Events"])
def create_events_endpoint(
    events: List[Event], db: Session = Depends(get_db)
):
    event_service = EventService(db)
    created_events = event_service.create_events(events)
    return {
        'message': f'se crearon {len(created_events)} eventos correctamente'
    }


@router.get("/api/events", summary="Obtener eventos", tags=["Events"])
def get_events_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    event_service = EventService(db)
    return event_service.get_events(session_id)


@router.get(
    "/api/stories", summary="Obtener stories", tags=["Stories"],
    response_model=List[Story]
)
def get_stories_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    story_service = StoryService(db)
    stories = story_service.get_stories(session_id)
    return stories


@router.get(
    "/api/tests", summary="Obtener tests", tags=["Tests"],
    response_model=List[Test]
)
def get_tests_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    test_service = TestService(db)
    tests = test_service.get_tests(session_id)
    return tests
