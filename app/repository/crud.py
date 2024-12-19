from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.repository.models import EventModel
from app.schemas.event import Event


def create_event(db: Session, event: Event):
    db_event = EventModel(
        event=event.event,
        properties=event.properties.model_dump(),
        timestamp=event.timestamp
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_events(db: Session, session_id: Optional[str] = None):
    query = db.query(EventModel)
    if session_id:
        query = query.filter(
            text(f'properties->>"session_id" = "{session_id}"')
        )
    return query.all()
