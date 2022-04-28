from fastapi import FastAPI

from . import models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}
