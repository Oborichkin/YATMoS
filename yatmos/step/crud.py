from typing import List

from sqlalchemy.orm import Session

from ..case.model import Case
from .model import Step
from .schema import StepCreate, StepUpdate


def get_step(db: Session, step_id: int):
    return db.query(Step).filter(Step.id == step_id).first()


def get_steps(db: Session, case_id: int):
    return db.query(Case).filter(Case.id == case_id).first().steps


def add_step(db: Session, step: StepCreate, case_id: int):
    case = db.query(Case).filter(Case.id == case_id).first()
    new_step = Step(**step.dict(), case_id=case_id)
    case.steps.append(new_step)
    db.commit()
    db.refresh(new_step)
    return new_step


def delete_step(db: Session, step_id: int):
    step = db.query(Step).filter(Step.id == step_id)
    step.delete()
    db.commit()


def update_step(db: Session, step_id: int, step: StepUpdate):
    upd_step = db.query(Step).filter(Step.id == step_id)
    upd_step.update(step.dict(exclude_unset=True))
    db.commit()
    upd_step = upd_step.first()
    db.refresh(upd_step)
    return upd_step


def reorder_steps(db: Session, case_id: int, permutation: List[int]):
    steps = db.query(Case).filter(Case.id == case_id).first().steps
    assert len(steps) == len(permutation)
    for i, step_id in enumerate(permutation):
        steps[i].position = len(steps) + step_id
    db.commit()
    steps.reorder()
    return db.query(Case).filter(Case.id == case_id).first().steps
