from fastapi import FastAPI
from app.repository.database import Base, engine
from app.api.routes import router

app = FastAPI(
    title="Test generator API",
    version="1.0",
    description="API generar test a partir de eventos de usuarios"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
