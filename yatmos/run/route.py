from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import Run, RunUpdate
from .crud import get_run, delete_run, update_run
from ..dependencies import get_db

router = APIRouter(prefix="/run", tags=["Run"])


@router.get("/{id}", response_model=Run, response_description="Run retrieved")
def get_run(id: int, db: Session = Depends(get_db)):
    run = get_run(db, run_id=id)
    if not run:
        raise HTTPException(404, "run not found")
    return run


@router.delete("/{id}")
def delete_run(id: int, db: Session = Depends(get_db)):
    run = delete_run(db, run_id=id)
    return run


@router.patch("/{id}")
def update_run(id: int, run: RunUpdate, db: Session = Depends(get_db)):
    return update_run(db, id, run)
