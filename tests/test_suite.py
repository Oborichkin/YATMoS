from .conftest import suite_a


def test_create_suite(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.post(f"/api/project/{x.id}/suite", json=suite_a)

    assert resp.status_code == 200
    assert resp.json()["title"] == suite_a["title"]
    assert resp.json()["desc"] == suite_a["desc"]
    assert resp.json()["id"]
    assert resp.json()["project_id"] == x.id


def test_get_project_suites(client, db_with_3_projects, db_with_3_suites):
    x, y, z = db_with_3_projects
    resp = client.get(f"/api/project/{x.id}/suites")
    assert resp.status_code == 200
    assert len(resp.json()) == 3


def test_delete_suite(client, db_with_3_suites):
    a, b, c = db_with_3_suites
    resp = client.delete(f"/api/suite/{a.id}")
    assert resp.status_code == 200
    resp = client.get(f"/api/suite/{a.id}")
    assert resp.status_code == 404


def test_update_suite(client, db_with_3_suites):
    a, b, c = db_with_3_suites
    resp = client.patch(f"/api/suite/{a.id}", json={"title": "Suite AAA"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Suite AAA"
    resp = client.get(f"/api/suite/{a.id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Suite AAA"
