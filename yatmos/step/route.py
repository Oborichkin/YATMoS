from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import Step, StepUpdate
from .crud import get_step, delete_step, update_step
from ..dependencies import get_db

router = APIRouter(prefix="/step", tags=["Step"])


@router.get("/{id}", response_model=Step, response_description="Step retrieved")
def get_step(id: int, db: Session = Depends(get_db)):
    step = get_step(db, step_id=id)
    if not step:
        raise HTTPException(404, "step not found")
    return step


@router.delete("/{id}")
def delete_step(id: int, db: Session = Depends(get_db)):
    step = delete_step(db, step_id=id)
    return step


@router.patch("/{id}")
def update_step(id: int, step: StepUpdate, db: Session = Depends(get_db)):
    return update_step(db, id, step)
