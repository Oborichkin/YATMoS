from sqlalchemy.orm import Session
from .model import Suite
from .schema import SuiteCreate, SuiteUpdate


def get_suite(db: Session, suite_id: int):
    return db.query(Suite).filter(Suite.id == suite_id).first()


def get_suites(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(Suite).filter(Suite.project_id == project_id).offset(skip).limit(limit).all()


def create_suite(db: Session, suite: SuiteCreate, project_id: int):
    new_suite = Suite(**suite.dict(), project_id=project_id)
    db.add(new_suite)
    db.commit()
    db.refresh(new_suite)
    return new_suite


def delete_suite(db: Session, suite_id: int):
    suite = db.query(Suite).filter(Suite.id == suite_id)
    suite.delete()
    db.commit()


def update_suite(db: Session, suite_id: int, suite: SuiteUpdate):
    upd_suite = db.query(Suite).filter(Suite.id == suite_id)
    upd_suite.update(suite.dict(exclude_unset=True))
    db.commit()
    upd_suite = upd_suite.first()
    db.refresh(upd_suite)
    return upd_suite
