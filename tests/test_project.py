import pytest

from .conftest import project_x


def test_create_project(client):
    resp = client.post("/project/", json=project_x)
    assert resp.status_code == 200
    assert resp.json()["title"] == project_x["title"]
    assert resp.json()["desc"] == project_x["desc"]
    assert resp.json()["id"]
    assert not resp.json()["test_suites"]


def test_get_empty_projects_list(client):
    resp = client.get("/project/")
    assert resp.status_code == 200
    assert resp.json() == []


def test_get_projects_list(client, db_with_3_projects):
    resp = client.get("/project/")
    assert resp.status_code == 200
    assert len(resp.json()) == 3


def test_get_one_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.get(f"/project/{x.id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == x.title
    assert resp.json()["desc"] == x.desc


def _test_update_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.put(f"/project/{x.id}", json={"title": "Project XXX"})
    assert resp.status_code == 200
    assert resp.json()["data"]
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def _test_delete_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.delete(f"/project/{x['id']}")
    assert resp.status_code == 200
    assert resp.json()["code"] == 200
    assert resp.json()["message"]
    resp = client.delete(f"/project/{x['id']}")
    assert resp.status_code == 200
    assert resp.json()["code"] == 404
    assert resp.json()["message"]
