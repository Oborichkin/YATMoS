from fastapi import FastAPI

from .database import engine, Base
from .project.route import router as project_router
from .test_suite.route import router as test_suite_router
from .test_case.route import router as test_case_router
from .test_step.route import router as test_step_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(project_router)
app.include_router(test_suite_router)
app.include_router(test_case_router)
app.include_router(test_step_router)


__version__ = "0.1.0"


@app.get("/", tags=["Root"])
def read_root():
    return {"version": __version__}
