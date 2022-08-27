from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud
from .schema import Case, CaseUpdate
from ..step.schema import Step, StepCreate
from ..step.crud import add_step, get_steps, reorder_steps
from ..dependencies import get_db

router = APIRouter(prefix="/case", tags=["Case"])


@router.get("/{id}", response_model=Case, response_description="Case retrieved")
def get_case(id: int, db: Session = Depends(get_db)):
    case = crud.get_case(db, case_id=id)
    if not case:
        raise HTTPException(404, "case not found")
    return case


@router.delete("/{id}")
def delete_case(id: int, db: Session = Depends(get_db)):
    case = crud.delete_case(db, case_id=id)
    return case


@router.patch("/{id}")
def update_case(id: int, case: CaseUpdate, db: Session = Depends(get_db)):
    return crud.update_case(db, id, case)


@router.post("/{id}/step", response_model=Step, response_description="Step created", tags=["Step"])
def create_step(id: int, step: StepCreate, db: Session = Depends(get_db)):
    return add_step(db, step, case_id=id)


@router.get(
    "/{id}/steps", response_model=List[Step], response_description="List of case steps", tags=["Step"]
)
def get_steps_for_case(id: int, db: Session = Depends(get_db)):
    return get_steps(db, case_id=id)


@router.patch(
    "/{id}/steps", response_model=List[Step], response_description="Reordered list of steps", tags=["Step"]
)
def reorder_steps_for_case(id: int, permutation: List[int], db: Session = Depends(get_db)):
    return reorder_steps(db, case_id=id, permutation=permutation)
