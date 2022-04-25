from fastapi import FastAPI

from . import routes, models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router, tags=["Project"], prefix="/project")


@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}
