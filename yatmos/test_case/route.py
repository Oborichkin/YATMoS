from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import TestCase, TestCaseUpdate
from .crud import get_test_case, delete_test_case, update_test_case
from ..dependencies import get_db

router = APIRouter(prefix="/case", tags=["Test Case"])


@router.get("/{id}", response_model=TestCase, response_description="Test Case retrieved")
def get_case(id: int, db: Session = Depends(get_db)):
    case = get_test_case(db, case_id=id)
    if not case:
        raise HTTPException(404, "Test case not found")
    return case


@router.delete("/{id}")
def delete_case(id: int, db: Session = Depends(get_db)):
    case = delete_test_case(db, case_id=id)
    return case


@router.patch("/{id}")
def update_case(id: int, case: TestCaseUpdate, db: Session = Depends(get_db)):
    return update_test_case(db, id, case)
