def test_create_run(client, db_with_3_steps, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.post(f"/project/{x.id}/run", json={"title": "Nightly run", "desc": "00:00 everyday run"})
    assert resp.status_code == 200, resp.reason
    assert resp.json()["title"] == "Nightly run"
    assert resp.json()["desc"] == "00:00 everyday run"
    assert resp.json()["id"]
    run_id = resp.json()["id"]
    assert resp.json()["project_id"] == x.id
    run_json = resp.json()

    resp = client.get(f"/project/{x.id}/runs")
    assert resp.status_code == 200, resp.reason
    assert len(resp.json()) == 1

    resp = client.get(f"/run/{run_id}")
    assert resp.status_code == 200, resp.reason
    assert resp.json() == run_json


def test_create_full_run(client, db_with_3_steps, db_with_3_projects):
    x, y, z = db_with_3_projects
    resp = client.post(f"/project/{x.id}/full_run", json={"title": "Nightly run", "desc": "00:00 everyday run"})
    assert resp.status_code == 200, resp.reason
    resp = client.get(f"/run/{resp.json()['id']}/results")
    assert resp.status_code == 200, resp.reason
    assert len(resp.json()) == 3


def test_delete_run(client, db_with_3_projects, db_with_3_runs):
    x, y, z = db_with_3_projects
    a, b, c = db_with_3_runs
    resp = client.get(f"/project/{x.id}/runs")
    assert len(resp.json()) == 3

    resp = client.delete(f"/run/{a.id}")
    assert resp.status_code == 200

    resp = client.get(f"/project/{x.id}/runs")
    assert len(resp.json()) == 2
    resp = client.get(f"/run/{a.id}")
    assert resp.status_code == 404


def test_update_run(client, db_with_3_runs):
    x, y, z = db_with_3_runs
    resp = client.patch(f"/run/{x.id}", json={"desc": "new description"})
    assert resp.status_code == 200
    assert resp.json()["desc"] == "new description"
    resp = client.get(f"/run/{x.id}")
    assert resp.status_code == 200
    assert resp.json()["desc"] == "new description"
