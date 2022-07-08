from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from .schema import TestCase, TestCaseUpdate
from .crud import get_test_case, delete_test_case, update_test_case
from ..test_step.schema import TestStep, TestStepCreate
from ..test_step.crud import add_test_step, get_test_steps
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


@router.post("/{id}/step", response_model=TestStep, response_description="Test step created", tags=["Test Step"])
def create_test_step(id: int, test_step: TestStepCreate, db: Session = Depends(get_db)):
    return add_test_step(db, test_step, case_id=id)


@router.get(
    "/{id}/steps", response_model=List[TestStep], response_description="List of test case steps", tags=["Test Step"]
)
def get_test_steps_for_case(id: int, db: Session = Depends(get_db)):
    return get_test_steps(db, case_id=id)
