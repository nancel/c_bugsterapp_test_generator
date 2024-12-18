from typing import Optional, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_event, get_events
from app.schemas.event import Event
from app.processors.event_processor import EventProcessor
from app.processors.story_processor import StoryProcessor

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/events", summary="Crear eventos", tags=["Events"])
def create_events_endpoint(
    events: List[Event], db: Session = Depends(get_db)
):
    created_events = 0
    for event in events:
        create_event(db, event)
        created_events += 1
    return {'message': f'se crearon {created_events} eventos correctamente'}


@router.get("/api/events", summary="Obtener eventos", tags=["Events"])
def get_events_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    return get_events(db, session_id)


@router.get("/api/stories", summary="Obtener stories", tags=["Stories"])
def get_stories_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    events = get_events(db, session_id)
    processor = EventProcessor()
    for event in events:
        processor.add_event(event)

    return {"stories": processor.generate_stories()}


@router.get("/api/tests", summary="Obtener tests", tags=["Tests"])
def get_tests_endpoint(
    session_id: Optional[str] = None, db: Session = Depends(get_db)
):
    events = get_events(db, session_id)
    event_processor = EventProcessor()
    for event in events:
        event_processor.add_event(event)
    stories = event_processor.generate_stories()
    story_processor = StoryProcessor(stories[0])

    return {"tests": story_processor.generate_test().strip()}
