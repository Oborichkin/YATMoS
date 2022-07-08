from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .schema import Project, ProjectCreate, ProjectUpdate
from .crud import create_project, get_project, get_projects, update_project, delete_project
from ..test_suite.schema import TestSuite, TestSuiteCreate
from ..test_suite.crud import get_test_suites, create_test_suite
from ..dependencies import get_db

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


@router.post("/{id}/suite", response_model=TestSuite, response_description="Test suite created", tags=["Test Suite"])
def add_test_suite(id: int, test_suite: TestSuiteCreate, db: Session = Depends(get_db)):
    return create_test_suite(db, test_suite, project_id=id)


@router.get(
    "/{id}/suites",
    response_model=List[TestSuite],
    response_description="List of project test suites",
    tags=["Test Suite"],
)
def get_test_suite_for_project(id: int, db: Session = Depends(get_db)):
    return get_test_suites(db, project_id=id)
