from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import TestStep, TestStepUpdate
from .crud import get_test_step, delete_test_step, update_test_step
from ..dependencies import get_db

router = APIRouter(prefix="/step", tags=["Test Step"])


@router.get("/{id}", response_model=TestStep, response_description="Test Step retrieved")
def get_step(id: int, db: Session = Depends(get_db)):
    step = get_test_step(db, step_id=id)
    if not step:
        raise HTTPException(404, "Test step not found")
    return step


@router.delete("/{id}")
def delete_step(id: int, db: Session = Depends(get_db)):
    step = delete_test_step(db, step_id=id)
    return step


@router.patch("/{id}")
def update_step(id: int, step: TestStepUpdate, db: Session = Depends(get_db)):
    return update_test_step(db, id, step)
