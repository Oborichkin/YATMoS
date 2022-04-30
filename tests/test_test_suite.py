from yatmos import schemas
from .conftest import test_suite_a


def test_create_test_suite(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.post(f"/project/{x.id}/suite", json=test_suite_a)

    assert resp.status_code == 200
    assert resp.json()["title"] == test_suite_a["title"]
    assert resp.json()["desc"] == test_suite_a["desc"]
    assert resp.json()["id"]
    assert resp.json()["project_id"] == x.id


def test_get_project_test_suites(client, db_with_3_projects, db_with_3_suites):
    x, y, z = db_with_3_projects
    resp = client.get(f"/project/{x.id}/suites")
    assert resp.status_code == 200


def test_delete_test_suite(client, db_with_3_suites):
    a, b, c = db_with_3_suites
    resp = client.delete(f"/suite/{a.id}")
    assert resp.status_code == 200
    resp = client.get(f"/suite/{a.id}")
    assert resp.status_code == 404


def test_update_test_suite(client, db_with_3_suites):
    a, b, c = db_with_3_suites
    resp = client.patch(f"/suite/{a.id}", json={"title": "Test Suite AAA"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Suite AAA"
    resp = client.get(f"/suite/{a.id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Suite AAA"
