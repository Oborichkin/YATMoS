from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(prefix="/suite", tags=["Test Suite"])


@router.post("/project/{id}/suite", response_model=schemas.TestSuite, response_description="Test suite created")
def create_test_suite(id: int, test_suite: schemas.TestSuiteCreate, db: Session = Depends(get_db)):
    return crud.create_test_suite(db, test_suite, project_id=id)


@router.get(
    "/project/{id}/suites", response_model=List[schemas.TestSuite], response_description="Test suites retrieved"
)
def get_project_suites(id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_test_suites(db, project_id=id, skip=skip, limit=limit)


@router.get("/suite/{id}", response_model=schemas.Project, response_description="Project retrieved")
def get_suite(id: int, db: Session = Depends(get_db)):
    suite = crud.get_test_suite(db, suite_id=id)
    if not suite:
        raise HTTPException(404, "Test suite not found")
    return suite


@router.delete("/suite/{id}")
def delete_suite(id: int, db: Session = Depends(get_db)):
    suite = crud.delete_test_suite(db, suite_id=id)
    return suite


@router.patch("/suite/{id}")
def update_suite(id: int, suite: schemas.TestSuiteUpdate, db: Session = Depends(get_db)):
    return crud.update_test_suite(db, id, suite)
