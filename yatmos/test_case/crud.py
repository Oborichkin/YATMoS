from sqlalchemy.orm import Session
from .model import TestCase
from .schema import TestCaseCreate, TestCaseUpdate


def get_test_case(db: Session, case_id: int):
    return db.query(TestCase).filter(TestCase.id == case_id).first()


def get_test_cases(db: Session, suite_id: int, skip: int = 0, limit: int = 100):
    return db.query(TestCase).filter(TestCase.suite_id == suite_id).offset(skip).limit(limit).all()


def create_test_case(db: Session, test_case: TestCaseCreate, suite_id: int):
    new_test_case = TestCase(**test_case.dict(), suite_id=suite_id)
    db.add(new_test_case)
    db.commit()
    db.refresh(new_test_case)
    return new_test_case


def delete_test_case(db: Session, case_id: int):
    case = db.query(TestCase).filter(TestCase.id == case_id)
    case.delete()
    db.commit()


def update_test_case(db: Session, case_id: int, case: TestCaseUpdate):
    upd_test_case = db.query(TestCase).filter(TestCase.id == case_id)
    upd_test_case.update(case.dict(exclude_unset=True))
    db.commit()
    upd_test_case = upd_test_case.first()
    db.refresh(upd_test_case)
    return upd_test_case
