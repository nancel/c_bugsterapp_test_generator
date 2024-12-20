from celery import Celery
from app.repository.database import SessionLocal
from app.services.event import EventService


celery_app = Celery("events")
celery_app.config_from_object("app.tasks.config")


@celery_app.task
def process_event(events):
    db = SessionLocal()
    try:
        event_service = EventService(db)
        event_service.create_events(events)
    except Exception:
        db.rollback()
    finally:
        db.close()
