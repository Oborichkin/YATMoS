import pytest

from fastapi.testclient import TestClient

from yatmos import app
from yatmos.project.crud import create_project
from yatmos.test_suite.crud import create_test_suite
from yatmos.dependencies import get_db
from yatmos.database import engine, SessionLocal, Base
from yatmos.project.schema import ProjectCreate
from yatmos.test_suite.schema import TestSuiteCreate


project_x = {"title": "Project X", "desc": "Secret project X"}
project_y = {"title": "Project Y", "desc": "Secret project Y"}
project_z = {"title": "Project Z", "desc": "Secret project Z"}

test_suite_a = {"title": "Test Suite A", "desc": "Main test suite"}
test_suite_b = {"title": "Test Suite B", "desc": "Secondary test suite"}
test_suite_c = {"title": "Test Suite C", "desc": "Performance test suite"}


@pytest.fixture(scope="function", autouse=True)
def empty_db():
    db = db = SessionLocal()
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
