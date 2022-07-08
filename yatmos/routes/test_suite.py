from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from ..schemas import Project, TestSuiteUpdate
from ..crud.test_suite import update_test_suite, delete_test_suite, get_test_suite
from ..dependencies import get_db

router = APIRouter(prefix="/suite", tags=["Test Suite"])


@router.get("/{id}", response_model=Project, response_description="Project retrieved")
def get_suite(id: int, db: Session = Depends(get_db)):
    suite = get_test_suite(db, suite_id=id)
    if not suite:
        raise HTTPException(404, "Test suite not found")
    return suite


@router.delete("/{id}")
def delete_suite(id: int, db: Session = Depends(get_db)):
    suite = delete_test_suite(db, suite_id=id)
    return suite


@router.patch("/{id}")
def update_suite(id: int, suite: TestSuiteUpdate, db: Session = Depends(get_db)):
    return update_test_suite(db, id, suite)
