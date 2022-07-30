from sqlalchemy.orm import Session
from .model import Run
from .schema import RunCreate, RunUpdate


def get_run(db: Session, run_id: int):
    return db.query(Run).filter(Run.id == run_id).first()


def get_runs(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(Run).filter(Run.project_id == project_id).offset(skip).limit(limit).all()


def create_run(db: Session, run: RunCreate, project_id: int):
    new_run = Run(**run.dict(), project_id=project_id)
    db.add(new_run)
    db.commit()
    db.refresh(new_run)
    return new_run


def delete_run(db: Session, run_id: int):
    run = db.query(Run).filter(Run.id == run_id)
    run.delete()
    db.commit()


def update_run(db: Session, run_id: int, run: RunUpdate):
    upd_run = db.query(Run).filter(Run.id == run_id)
    upd_run.update(run.dict(exclude_unset=True))
    db.commit()
    upd_run = upd_run.first()
    db.refresh(upd_run)
    return upd_run
