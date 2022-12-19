from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import __version__
from .graphql import graphql_app
from .database import engine, Base
from .project.route import router as project_router
from .suite.route import router as suite_router
from .case.route import router as case_router
from .step.route import router as step_router
from .run.route import router as run_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(project_router)
app.include_router(suite_router)
app.include_router(case_router)
app.include_router(step_router)
app.include_router(run_router)
app.include_router(graphql_app, prefix="/graphql")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


@app.get("/", tags=["Root"])
def read_root():
    return {"version": __version__}
