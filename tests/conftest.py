import pytest
import pytest_asyncio
import asyncio

from fastapi.testclient import TestClient

from yatmos import app
from yatmos.models.project import add_project
from yatmos.database import projects


project_x = {"title": "Project X"}
project_y = {"title": "Project Y"}
project_z = {"title": "Project Z"}


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clear_database_before_and_after_test():
    await projects.drop()
    yield
    await projects.drop()


@pytest.fixture()
def client():
    return TestClient(app)


@pytest_asyncio.fixture
async def db_with_3_projects():
    x = await add_project(project_x)
    y = await add_project(project_y)
    z = await add_project(project_z)
    yield x, y, z
