from fastapi import FastAPI

from . import models, schemas
from .database import engine, Base
from .routes import project, test_suite

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(project.router)
app.include_router(test_suite.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}
