from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .schema import Suite, SuiteUpdate
from .crud import update_suite, delete_suite, get_suite
from ..case.schema import Case, CaseCreate
from ..case.crud import create_case, get_cases
from ..dependencies import get_db

router = APIRouter(prefix="/suite", tags=["Suite"])


@router.get("/{id}", response_model=Suite, response_description="Suite retrieved")
def get_suite(id: int, db: Session = Depends(get_db)):
    suite = get_suite(db, suite_id=id)
    if not suite:
        raise HTTPException(404, "suite not found")
    return suite


@router.delete("/{id}")
def delete_suite(id: int, db: Session = Depends(get_db)):
    suite = delete_suite(db, suite_id=id)
    return suite


@router.patch("/{id}")
def update_suite(id: int, suite: SuiteUpdate, db: Session = Depends(get_db)):
    return update_suite(db, id, suite)


@router.post("/{id}/case", response_model=Case, response_description="Case created", tags=["Case"])
def add_case(id: int, case: CaseCreate, db: Session = Depends(get_db)):
    return create_case(db, case, suite_id=id)


@router.get(
    "/{id}/cases", response_model=List[Case], response_description="List of suite cases", tags=["Case"]
)
def get_cases_for_suite(id: int, db: Session = Depends(get_db)):
    return get_cases(db, suite_id=id)
