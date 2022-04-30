from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, crud, schemas, app
from .database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/project", response_model=schemas.Project, response_description="Project data added to database")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    # Check if project with same title exists
    return crud.create_project(db, project=project)


@app.get("/projects", response_model=List[schemas.Project], response_description="Projects retrieved")
def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)


@app.get("/project/{id}", response_model=schemas.Project, response_description="Project retrieved")
def get_project(id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id=id)
    if not project:
        raise HTTPException(404, "Project not found")
    return project


@app.patch("/project/{id}", response_model=schemas.Project, response_description="Project updated")
def update_project(id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    return crud.update_project(db, project_id=id, project=project)


@app.delete("/project/{id}", response_description="Project deleted")
def delete_project(id: int, db: Session = Depends(get_db)):
    project = crud.delete_project(db, project_id=id)
    return project


@app.post("/project/{id}/suite", response_model=schemas.TestSuite, response_description="Test suite created")
def create_test_suite(id: int, test_suite: schemas.TestSuiteCreate, db: Session = Depends(get_db)):
    return crud.create_test_suite(db, test_suite, project_id=id)


@app.get("/project/{id}/suites", response_model=List[schemas.TestSuite], response_description="Test suites retrieved")
def get_project_suites(id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_test_suites(db, project_id=id, skip=skip, limit=limit)


@app.get("/suite/{id}", response_model=schemas.Project, response_description="Project retrieved")
def get_suite(id: int, db: Session = Depends(get_db)):
    suite = crud.get_test_suite(db, suite_id=id)
    if not suite:
        raise HTTPException(404, "Test suite not found")
    return suite


@app.delete("/suite/{id}")
def delete_suite(id: int, db: Session = Depends(get_db)):
    suite = crud.delete_test_suite(db, suite_id=id)
    return suite


@app.patch("/suite/{id}")
def update_suite(id: int, suite: schemas.TestSuiteUpdate, db: Session = Depends(get_db)):
    return crud.update_test_suite(db, id, suite)
