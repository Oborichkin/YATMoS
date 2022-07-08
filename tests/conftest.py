import pytest

from fastapi.testclient import TestClient

from yatmos import app
from yatmos.dependencies import get_db
from yatmos.database import engine, SessionLocal, Base
from yatmos.project.crud import create_project
from yatmos.project.schema import ProjectCreate
from yatmos.test_suite.schema import TestSuiteCreate
from yatmos.test_suite.crud import create_test_suite
from yatmos.test_case.crud import create_test_case
from yatmos.test_case.schema import TestCaseCreate
from yatmos.test_step.crud import add_test_step
from yatmos.test_step.schema import TestStepCreate


project_x = {"title": "Project X", "desc": "Secret project X"}
project_y = {"title": "Project Y", "desc": "Secret project Y"}
project_z = {"title": "Project Z", "desc": "Secret project Z"}

test_suite_a = {"title": "Test Suite A", "desc": "Main test suite"}
test_suite_b = {"title": "Test Suite B", "desc": "Secondary test suite"}
test_suite_c = {"title": "Test Suite C", "desc": "Performance test suite"}

test_case_a = {"title": "Test Case A", "desc": "First test case"}
test_case_b = {"title": "Test Case B", "desc": "Second test case"}
test_case_c = {"title": "Test Case C", "desc": "Third test case"}

test_step_a = {"title": "Test Step A", "desc": "First test step"}
test_step_b = {"title": "Test Step B", "desc": "Second test step"}
test_step_c = {"title": "Test Step C", "desc": "Third test step"}


@pytest.fixture(scope="function", autouse=True)
def empty_db():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    yield db
    Base.metadata.drop_all(bind=engine)
    db.close()


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture
def db_with_3_projects(empty_db):
    x = create_project(empty_db, ProjectCreate(**project_x))
    y = create_project(empty_db, ProjectCreate(**project_y))
    z = create_project(empty_db, ProjectCreate(**project_z))
    yield x, y, z


@pytest.fixture
def db_with_3_suites(empty_db, db_with_3_projects):
    x, y, z = db_with_3_projects
    a = create_test_suite(empty_db, TestSuiteCreate(**test_suite_a), x.id)
    b = create_test_suite(empty_db, TestSuiteCreate(**test_suite_b), x.id)
    c = create_test_suite(empty_db, TestSuiteCreate(**test_suite_c), x.id)
    yield a, b, c


@pytest.fixture
def db_with_3_cases(empty_db, db_with_3_suites):
    a, b, c = db_with_3_suites
    a1 = create_test_case(empty_db, TestCaseCreate(**test_case_a), a.id)
    b1 = create_test_case(empty_db, TestCaseCreate(**test_case_b), a.id)
    c1 = create_test_case(empty_db, TestCaseCreate(**test_case_c), a.id)
    yield a1, b1, c1


@pytest.fixture
def db_with_3_steps(empty_db, db_with_3_cases):
    a, b, c = db_with_3_cases
    a1 = add_test_step(empty_db, TestStepCreate(**test_step_a), a.id)
    b1 = add_test_step(empty_db, TestStepCreate(**test_step_b), a.id)
    c1 = add_test_step(empty_db, TestStepCreate(**test_step_c), a.id)
    yield a1, b1, c1
