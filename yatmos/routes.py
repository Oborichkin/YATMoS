from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, crud, schemas
from .database import SessionLocal, engine

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
        raise HTTPException(404, "User not found")
    return project
