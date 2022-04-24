from fastapi import FastAPI

from .routes import ProjectRouter

app = FastAPI()

app.include_router(ProjectRouter, tags=["Project"], prefix="/project")


@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}
