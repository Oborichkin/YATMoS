from sqlalchemy.orm import Session
from ..test_case.model import TestCase
from .model import TestStep
from .schema import TestStepCreate, TestStepUpdate


def get_test_step(db: Session, step_id: int):
    return db.query(TestStep).filter(TestStep.id == step_id).first()


def get_test_steps(db: Session, case_id: int):
    return db.query(TestCase).filter(TestCase.id == case_id).first().steps


def add_test_step(db: Session, test_step: TestStepCreate, case_id: int):
    test_case = db.query(TestCase).filter(TestCase.id == case_id).first()
    new_test_step = TestStep(**test_step.dict(), case_id=case_id)
    test_case.steps.append(new_test_step)
    db.commit()
    db.refresh(new_test_step)
    return new_test_step


def delete_test_step(db: Session, step_id: int):
    step = db.query(TestStep).filter(TestStep.id == step_id)
    step.delete()
    db.commit()


def update_test_step(db: Session, step_id: int, step: TestStepUpdate):
    upd_test_step = db.query(TestStep).filter(TestStep.id == step_id)
    upd_test_step.update(step.dict(exclude_unset=True))
    db.commit()
    upd_test_step = upd_test_step.first()
    db.refresh(upd_test_step)
    return upd_test_step
