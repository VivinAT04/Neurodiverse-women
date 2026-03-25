from fastapi import FastAPI
from app.db import engine, Base
from app import models
from app.routes import users, moods, tasks, assistant

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(moods.router)
app.include_router(tasks.router)
app.include_router(assistant.router)


@app.get("/")
def read_root():
    return {"message": "Aksess backend is running"}