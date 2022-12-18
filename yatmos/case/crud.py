from sqlalchemy.orm import Session
from .model import Case, CaseResult
from .schema import CaseCreate, CaseUpdate


def get_case(db: Session, case_id: int):
    return db.query(Case).filter(Case.id == case_id).first()


def get_case_result(db: Session, case_id: int):
    return db.query(CaseResult).filter(CaseResult.id == case_id).first()


def get_cases(db: Session, suite_id: int, skip: int = 0, limit: int = 100):
    return db.query(Case).filter(Case.suite_id == suite_id).offset(skip).limit(limit).all()


def create_case(db: Session, case: CaseCreate, suite_id: int):
    new_case = Case(**case.dict(), suite_id=suite_id)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return new_case


def delete_case(db: Session, case_id: int):
    case = db.query(Case).filter(Case.id == case_id)
    case.delete()
    db.commit()


def update_case(db: Session, case_id: int, case: CaseUpdate):
    upd_case = db.query(Case).filter(Case.id == case_id)
    upd_case.update(case.dict(exclude_unset=True))
    db.commit()
    upd_case = upd_case.first()
    db.refresh(upd_case)
    return upd_case
