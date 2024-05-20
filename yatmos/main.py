from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

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

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
