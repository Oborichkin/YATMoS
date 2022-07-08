from sqlalchemy.orm import Session
from .model import TestSuite
from .schema import TestSuiteCreate, TestSuiteUpdate


def get_test_suite(db: Session, suite_id: int):
    return db.query(TestSuite).filter(TestSuite.id == suite_id).first()


def get_test_suites(db: Session, project_id: int, skip: int = 0, limit: int = 100):
    return db.query(TestSuite).filter(TestSuite.project_id == project_id).offset(skip).limit(limit).all()


def create_test_suite(db: Session, test_suite: TestSuiteCreate, project_id: int):
    new_test_suite = TestSuite(**test_suite.dict(), project_id=project_id)
    db.add(new_test_suite)
    db.commit()
    db.refresh(new_test_suite)
    return new_test_suite


def delete_test_suite(db: Session, suite_id: int):
    suite = db.query(TestSuite).filter(TestSuite.id == suite_id)
    suite.delete()
    db.commit()


def update_test_suite(db: Session, suite_id: int, suite: TestSuiteUpdate):
    upd_test_suite = db.query(TestSuite).filter(TestSuite.id == suite_id)
    upd_test_suite.update(suite.dict(exclude_unset=True))
    db.commit()
    upd_test_suite = upd_test_suite.first()
    db.refresh(upd_test_suite)
    return upd_test_suite
