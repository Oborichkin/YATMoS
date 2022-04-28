from .conftest import test_suite_a


def test_create_project(client, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.post(f"/project/{x.id}/suite", json=test_suite_a)

    assert resp.status_code == 200
    assert resp.json()["title"] == test_suite_a["title"]
    assert resp.json()["desc"] == test_suite_a["desc"]
    assert resp.json()["id"]
    assert resp.json()["project_id"] == x.id
