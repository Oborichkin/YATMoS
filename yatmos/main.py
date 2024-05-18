from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from . import __version__
from .database import engine, Base
from .project.route import router as project_router
from .suite.route import router as suite_router
from .case.route import router as case_router
from .step.route import router as step_router
from .run.route import router as run_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

api_subpath = APIRouter(prefix="/api")
api_subpath.include_router(project_router)
api_subpath.include_router(suite_router)
api_subpath.include_router(case_router)
api_subpath.include_router(step_router)
api_subpath.include_router(run_router)

app.include_router(api_subpath)

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
