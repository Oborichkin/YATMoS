from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import TestRun, TestRunUpdate
from .crud import get_test_run, delete_test_run, update_test_run
from ..dependencies import get_db

router = APIRouter(prefix="/run", tags=["Test Run"])


@router.get("/{id}", response_model=TestRun, response_description="Test run retrieved")
def get_run(id: int, db: Session = Depends(get_db)):
    run = get_test_run(db, run_id=id)
    if not run:
        raise HTTPException(404, "Test run not found")
    return run


@router.delete("/{id}")
def delete_run(id: int, db: Session = Depends(get_db)):
    run = delete_test_run(db, run_id=id)
    return run


@router.patch("/{id}")
def update_run(id: int, run: TestRunUpdate, db: Session = Depends(get_db)):
    return update_test_run(db, id, run)
