from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .schema import TestSuite, TestSuiteUpdate
from .crud import update_test_suite, delete_test_suite, get_test_suite
from ..test_case.schema import TestCase, TestCaseCreate
from ..test_case.crud import create_test_case, get_test_cases
from ..dependencies import get_db

router = APIRouter(prefix="/suite", tags=["Test Suite"])


@router.get("/{id}", response_model=TestSuite, response_description="Test Suite retrieved")
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


@router.post("/{id}/case", response_model=TestCase, response_description="Test case created", tags=["Test Case"])
def add_test_case(id: int, test_case: TestCaseCreate, db: Session = Depends(get_db)):
    return create_test_case(db, test_case, suite_id=id)


@router.get(
    "/{id}/cases", response_model=List[TestCase], response_description="List of suite test cases", tags=["Test Case"]
)
def get_test_cases_for_suite(id: int, db: Session = Depends(get_db)):
    return get_test_cases(db, suite_id=id)
