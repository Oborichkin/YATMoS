from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/project", tags=["Project"])


@router.post("/", response_model=schemas.Project, response_description="Project data added to database")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # Check if project with same title exists
    return crud.create_project(db, project=project)


@router.get("/", response_model=List[schemas.Project], response_description="Projects retrieved")
def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=schemas.Project, response_description="Project retrieved")
def get_project(id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id=id)
    if not project:
        raise HTTPException(404, "Project not found")
    return project


@router.patch("/{id}", response_model=schemas.Project, response_description="Project updated")
def update_project(id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    return crud.update_project(db, project_id=id, project=project)


@router.delete("/{id}", response_description="Project deleted")
def delete_project(id: int, db: Session = Depends(get_db)):
    project = crud.delete_project(db, project_id=id)
    return project
