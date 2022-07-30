from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .schema import Project, ProjectCreate, ProjectUpdate
from .crud import create_project, get_project, get_projects, update_project, delete_project
from ..dependencies import get_db

# Suites
from ..suite.schema import Suite, SuiteCreate
from ..suite.crud import get_suites, create_suite

# Runs
from ..run.schema import Run, RunCreate
from ..run.crud import get_runs, create_run

router = APIRouter(prefix="/project", tags=["Project"])


@router.post("/", response_model=Project, response_description="Project data added to database")
def add_project(project: ProjectCreate, db: Session = Depends(get_db)):
    # Check if project with same title exists
    return create_project(db, project=project)


@router.get("/", response_model=List[Project], response_description="Projects retrieved")
@router.get("s/", response_model=List[Project], response_description="Projects retrieved")
def get_projects_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_projects(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=Project, response_description="Project retrieved")
def get_project_info(id: int, db: Session = Depends(get_db)):
    project = get_project(db, project_id=id)
    if not project:
        raise HTTPException(404, "Project not found")
    return project


@router.patch("/{id}", response_model=Project, response_description="Project updated")
def update_project_info(id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    return update_project(db, project_id=id, project=project)


@router.delete("/{id}", response_description="Project deleted")
def remove_project(id: int, db: Session = Depends(get_db)):
    project = delete_project(db, project_id=id)
    return project


@router.post("/{id}/suite", response_model=Suite, response_description="Suite created", tags=["Suite"])
def add_suite(id: int, suite: SuiteCreate, db: Session = Depends(get_db)):
    return create_suite(db, suite, project_id=id)


@router.get(
    "/{id}/suites",
    response_model=List[Suite],
    response_description="List of project suites",
    tags=["Suite"],
)
def get_suite_for_project(id: int, db: Session = Depends(get_db)):
    return get_suites(db, project_id=id)


@router.post("/{id}/run", response_model=Run, response_description="Run created", tags=["Run"])
def add_run(id: int, run: RunCreate, db: Session = Depends(get_db)):
    return create_run(db, run, project_id=id)


@router.get(
    "/{id}/runs",
    response_model=List[Run],
    response_description="List of project test runs",
    tags=["Run"],
)
def get_runs_for_project(id: int, db: Session = Depends(get_db)):
    return get_runs(db, project_id=id)
