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


def delete_project(db: Session, project_id: int):
    project = db.query(models.Project).filter(models.Project.id == project_id)
    project.delete()
    db.commit()


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate):
    upd_project = db.query(models.Project).filter(models.Project.id == project_id)
    upd_project.update(project.dict(exclude_unset=True))
    db.commit()
    upd_project = upd_project.first()
    db.refresh(upd_project)
    return upd_project


def get_test_suite(db: Session, suite_id: int):
    return db.query(models.TestSuite).filter(models.TestSuite.id == suite_id).first()


def get_test_suites(db: Session, project_id: int, skip: int = 0, limit: int = 0):
    return db.query(models.TestSuite).filter(models.TestSuite.project_id == project_id).offset(skip).limit(limit).all()


def create_test_suite(db: Session, test_suite: schemas.TestSuiteCreate, project_id: int):
    new_test_suite = models.TestSuite(**test_suite.dict(), project_id=project_id)
    db.add(new_test_suite)
    db.commit()
    db.refresh(new_test_suite)
    return new_test_suite


def delete_test_suite(db: Session, suite_id: int):
    suite = db.query(models.TestSuite).filter(models.TestSuite.id == suite_id)
    suite.delete()
    db.commit()


def update_test_suite(db: Session, suite_id: int, suite: schemas.TestSuiteUpdate):
    upd_test_suite = db.query(models.TestSuite).filter(models.TestSuite.id == suite_id)
    upd_test_suite.update(suite.dict(exclude_unset=True))
    db.commit()
    upd_test_suite = upd_test_suite.first()
    db.refresh(upd_test_suite)
    return upd_test_suite
