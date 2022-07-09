from sqlalchemy.orm import Session
from .model import TestRun
from .schema import TestRunCreate, TestRunUpdate


def get_test_run(db: Session, run_id: int):
    return db.query(TestRun).filter(TestRun.id == run_id).first()


def get_test_runs(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(TestRun).filter(TestRun.project_id == project_id).offset(skip).limit(limit).all()


def create_test_run(db: Session, test_run: TestRunCreate, project_id: int):
    new_test_run = TestRun(**test_run.dict(), project_id=project_id)
    db.add(new_test_run)
    db.commit()
    db.refresh(new_test_run)
    return new_test_run


def delete_test_run(db: Session, run_id: int):
    run = db.query(TestRun).filter(TestRun.id == run_id)
    run.delete()
    db.commit()


def update_test_run(db: Session, run_id: int, run: TestRunUpdate):
    upd_test_run = db.query(TestRun).filter(TestRun.id == run_id)
    upd_test_run.update(run.dict(exclude_unset=True))
    db.commit()
    upd_test_run = upd_test_run.first()
    db.refresh(upd_test_run)
    return upd_test_run
