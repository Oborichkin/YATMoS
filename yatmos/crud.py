from sqlalchemy.orm import Session
from . import models, schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()


def create_project(db: Session, project: schemas.ProjectCreate):
    new_project = models.Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_test_suites(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.TestSuite).offset(skip).limit(limit).all()


def create_test_suite(db: Session, test_suite: schemas.TestSuiteCreate, project_id: int):
    new_test_suite = models.TestSuite(**test_suite.dict(), project_id=project_id)
    db.add(new_test_suite)
    db.commit()
    db.refresh(new_test_suite)
    return new_test_suite
