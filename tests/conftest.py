import pytest

from fastapi.testclient import TestClient

from yatmos import app
from yatmos.crud import create_project
from yatmos.routes import get_db
from yatmos.models import Base
from yatmos.database import engine, SessionLocal
from yatmos.schemas import ProjectCreate


project_x = {"title": "Project X", "desc": "Secret project X"}
project_y = {"title": "Project Y", "desc": "Secret project Y"}
project_z = {"title": "Project Z", "desc": "Secret project Z"}

test_suite_a = {"title": "Test Suite A", "desc": "Main test suite"}


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
