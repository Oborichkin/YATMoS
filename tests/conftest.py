import pytest

from fastapi.testclient import TestClient

from yatmos.main import app
from yatmos.dependencies import get_db
from yatmos.database import engine, SessionLocal, Base
from yatmos.project.crud import create_project
from yatmos.project.schema import ProjectCreate
from yatmos.suite.schema import SuiteCreate
from yatmos.suite.crud import create_suite
from yatmos.case.crud import create_case
from yatmos.case.schema import CaseCreate
from yatmos.step.crud import add_step
from yatmos.step.schema import StepCreate
from yatmos.run.crud import create_run
from yatmos.run.schema import RunCreate


project_x = {"title": "Project X", "desc": "Secret project X"}
project_y = {"title": "Project Y", "desc": "Secret project Y"}
project_z = {"title": "Project Z", "desc": "Secret project Z"}

run_x = {"title": "Nightly", "desc": "Nightly run"}
run_y = {"title": "Release", "desc": "Release run"}
run_z = {"title": "Smoke", "desc": "Smoke tests run"}

suite_a = {"title": "Suite A", "desc": "Main suite"}
suite_b = {"title": "Suite B", "desc": "Secondary suite"}
suite_c = {"title": "Suite C", "desc": "Performance suite"}

case_a = {"title": "Case A", "desc": "First case"}
case_b = {"title": "Case B", "desc": "Second case"}
case_c = {"title": "Case C", "desc": "Third case"}

step_a = {"title": "Step A", "desc": "First step"}
step_b = {"title": "Step B", "desc": "Second step"}
step_c = {"title": "Step C", "desc": "Third step"}


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
    a = create_suite(empty_db, SuiteCreate(**suite_a), x.id)
    b = create_suite(empty_db, SuiteCreate(**suite_b), x.id)
    c = create_suite(empty_db, SuiteCreate(**suite_c), x.id)
    yield a, b, c


@pytest.fixture
def db_with_3_cases(empty_db, db_with_3_suites):
    a, b, c = db_with_3_suites
    a1 = create_case(empty_db, CaseCreate(**case_a), a.id)
    b1 = create_case(empty_db, CaseCreate(**case_b), a.id)
    c1 = create_case(empty_db, CaseCreate(**case_c), a.id)
    yield a1, b1, c1


@pytest.fixture
def db_with_3_steps(empty_db, db_with_3_cases):
    a, b, c = db_with_3_cases
    a1 = add_step(empty_db, StepCreate(**step_a), a.id)
    b1 = add_step(empty_db, StepCreate(**step_b), a.id)
    c1 = add_step(empty_db, StepCreate(**step_c), a.id)
    yield a1, b1, c1


@pytest.fixture
def db_with_3_runs(empty_db, db_with_3_projects, db_with_3_cases):
    x, y, z = db_with_3_projects
    x1 = create_run(empty_db, RunCreate(**run_x), x.id)
    y1 = create_run(empty_db, RunCreate(**run_y), x.id)
    z1 = create_run(empty_db, RunCreate(**run_z), x.id)
    yield x1, y1, z1
