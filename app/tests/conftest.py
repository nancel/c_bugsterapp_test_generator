import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.database import Base
from app.main import app
from app.routes import get_db
from app.schemas.event import Event, EventProperties
from app.models import EventModel
from app.schemas.story import Story
from fastapi.testclient import TestClient


@pytest.fixture(name="session", scope="session")
def session_fixture():
    test_engine = create_engine(
        "sqlite:///./test_events.db",
        connect_args={"check_same_thread": False}
    )
    TestSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(name="client", scope="session")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture
def sample_events():
    return [
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="email",
                    type="email"
                )
            ),
            timestamp="2024-12-16T10:00:00Z"
        ),
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="password",
                    type="password"
                )
            ),
            timestamp="2024-12-16T10:00:15Z"
        ),
        EventModel(
            event="$click",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="click",
                element_type="button",
                element_text="Log In",
                element_attributes=dict(
                    id="login-button",
                )
            ),
            timestamp="2024-12-16T10:00:30Z"
        ),
        EventModel(
            event="$api-call",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/login",
                host="example.com",
                pathname="/login",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="",
                element_type="",
                element_text="",
                element_attributes=dict(
                    api_url="https://api.example.com/login",
                    method="POST",
                    status="200",
                )
            ),
            timestamp="2024-12-16T10:00:35Z"
        ),
        EventModel(
            event="$navigation",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="navigation",
                element_type="",
                element_text="",
                element_attributes=None
            ),
            timestamp="2024-12-16T10:00:40Z"
        ),
        EventModel(
            event="$input",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="input",
                element_type="input",
                element_text="",
                element_attributes=dict(
                    id="display-name",
                    type="text"
                )
            ),
            timestamp="2024-12-16T10:00:60Z"
        ),
        EventModel(
            event="$click",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="click",
                element_type="button",
                element_text="Save",
                element_attributes=dict(
                    id="save-profile",
                )
            ),
            timestamp="2024-12-16T10:00:90Z"
        ),
        EventModel(
            event="$api-call",
            properties=dict(
                distinct_id="user_12345",
                session_id="session_67890",
                journey_id="journey_001",
                current_url="https://example.com/profile",
                host="example.com",
                pathname="/profile",
                browser="Chrome",
                device="Desktop",
                screen_height=1080,
                screen_width=1920,
                event_type="",
                element_type="",
                element_text="",
                element_attributes=dict(
                    api_url="https://api.example.com/profile",
                    method="PUT",
                    status="200",
                )
            ),
            timestamp="2024-12-16T10:00:95Z"
        ),
    ]


@pytest.fixture
def sample_story():
    return Story(
        name='login Log In',
        actions=[
            Event(
                event="$input",
                properties=EventProperties(
                    distinct_id="user_12345",
                    session_id="session_67890",
                    journey_id="journey_001",
                    current_url="https://example.com/login",
                    host="example.com",
                    pathname="/login",
                    browser="Chrome",
                    device="Desktop",
                    screen_height=1080,
                    screen_width=1920,
                    event_type="input",
                    element_type="input",
                    element_text="",
                    element_attributes=dict(
                        id="email",
                        type="email"
                    )
                ),
                timestamp="2024-12-16T10:00:00Z"
            ),
            Event(
                event="$input",
                properties=EventProperties(
                    distinct_id="user_12345",
                    session_id="session_67890",
                    journey_id="journey_001",
                    current_url="https://example.com/login",
                    host="example.com",
                    pathname="/login",
                    browser="Chrome",
                    device="Desktop",
                    screen_height=1080,
                    screen_width=1920,
                    event_type="input",
                    element_type="input",
                    element_text="",
                    element_attributes=dict(
                        id="password",
                        type="password"
                    )
                ),
                timestamp="2024-12-16T10:00:15Z"
            ),
            Event(
                event="$click",
                properties=EventProperties(
                    distinct_id="user_12345",
                    session_id="session_67890",
                    journey_id="journey_001",
                    current_url="https://example.com/login",
                    host="example.com",
                    pathname="/login",
                    browser="Chrome",
                    device="Desktop",
                    screen_height=1080,
                    screen_width=1920,
                    event_type="click",
                    element_type="button",
                    element_text="Log In",
                    element_attributes=dict(
                        id="login-button",
                    )
                ),
                timestamp="2024-12-16T10:00:30Z"
            ),
            Event(
                event="$api-call",
                properties=EventProperties(
                    distinct_id="user_12345",
                    session_id="session_67890",
                    journey_id="journey_001",
                    current_url="https://example.com/login",
                    host="example.com",
                    pathname="/login",
                    browser="Chrome",
                    device="Desktop",
                    screen_height=1080,
                    screen_width=1920,
                    event_type="",
                    element_type="",
                    element_text="",
                    element_attributes=dict(
                        api_url="https://api.example.com/login",
                        method="POST",
                        status="200",
                    )
                ),
                timestamp="2024-12-16T10:00:35Z"
            ),
            Event(
                event="$navigation",
                properties=EventProperties(
                    distinct_id="user_12345",
                    session_id="session_67890",
                    journey_id="journey_001",
                    current_url="https://example.com/profile",
                    host="example.com",
                    pathname="/profile",
                    browser="Chrome",
                    device="Desktop",
                    screen_height=1080,
                    screen_width=1920,
                    event_type="navigation",
                    element_type="",
                    element_text="",
                    element_attributes=None
                ),
                timestamp="2024-12-16T10:00:40Z"
            ),
        ]
    )
