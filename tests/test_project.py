import pytest


def test_create_project(client):
    resp = client.post("/project/", json={"title": "Project X", "desc": "Secret project"})
    assert resp.status_code == 200
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def test_get_empty_projects_list(client):
    resp = client.get("/project/")
    assert resp.status_code == 200
    assert resp.json()["data"] == []
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def test_get_projects_list(client, db_with_3_projects):
    resp = client.get("/project/")
    assert resp.status_code == 200
    assert len(resp.json()["data"]) == 3
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def test_get_one_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.get(f"/project/{x['id']}")
    assert resp.status_code == 200
    assert resp.json()["data"] == x
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def test_update_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.put(f"/project/{x['id']}", json={"title": "Project XXX"})
    assert resp.status_code == 200
    assert resp.json()["data"]
    assert resp.json()["code"] == 200
    assert resp.json()["message"]


def test_delete_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.delete(f"/project/{x['id']}")
    assert resp.status_code == 200
    assert resp.json()["code"] == 200
    assert resp.json()["message"]
    resp = client.delete(f"/project/{x['id']}")
    assert resp.status_code == 200
    assert resp.json()["code"] == 404
    assert resp.json()["message"]