import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient
from app.database import Base
from app.main import app
from app.routes import get_db
from app.tests.data.stories import get_stories
from app.tests.data.db_events import get_db_events
from app.tests.data.events import get_events


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
def sample_db_events():
    return get_db_events()


@pytest.fixture
def sample_stories():
    return get_stories()


@pytest.fixture
def sample_tests():
    return get_events()
