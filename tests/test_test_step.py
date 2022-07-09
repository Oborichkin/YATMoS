from .conftest import test_step_a, test_step_b, test_step_c


def test_create_test_step(client, db_with_3_cases):
    a, b, c = db_with_3_cases
    resp = client.post(f"/case/{a.id}/step", json=test_step_a)

    assert resp.status_code == 200
    assert resp.json()["title"] == test_step_a["title"]
    assert resp.json()["desc"] == test_step_a["desc"]
    assert resp.json()["id"]
    assert resp.json()["case_id"] == a.id

    resp = client.get(f"/step/{resp.json()['id']}")
    assert resp.status_code == 200


def test_get_case_test_steps(client, db_with_3_cases, db_with_3_steps):
    a, b, c = db_with_3_cases
    resp = client.get(f"/case/{a.id}/steps")
    assert resp.status_code == 200
    assert len(resp.json()) == 3
    a, b, c = db_with_3_steps
    assert resp.json()[0]["title"] == test_step_a["title"]
    assert resp.json()[1]["title"] == test_step_b["title"]
    assert resp.json()[2]["title"] == test_step_c["title"]


def test_delete_test_step(client, db_with_3_steps):
    a, b, c = db_with_3_steps
    resp = client.delete(f"/step/{a.id}")
    assert resp.status_code == 200
    resp = client.get(f"/step/{a.id}")
    assert resp.status_code == 404


def test_update_test_step(client, db_with_3_steps):
    a, b, c = db_with_3_steps
    resp = client.patch(f"/step/{a.id}", json={"title": "Test Step AAA"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Step AAA"
    resp = client.get(f"/step/{a.id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Step AAA"


def test_update_step_order(client, db_with_3_cases, db_with_3_steps):
    a, b, c = db_with_3_cases
    resp = client.get(f"/case/{a.id}/steps")
    assert resp.status_code == 200
    assert len(resp.json()) == 3
    assert resp.json()[0]["title"] == test_step_a["title"]
    assert resp.json()[1]["title"] == test_step_b["title"]
    assert resp.json()[2]["title"] == test_step_c["title"]

    resp = client.patch(f"/case/{a.id}/steps", json=[3, 2, 1])
    assert resp.status_code == 200
    assert len(resp.json()) == 3
    assert resp.json()[2]["title"] == test_step_a["title"]
    assert resp.json()[1]["title"] == test_step_b["title"]
    assert resp.json()[0]["title"] == test_step_c["title"]

    resp = client.get(f"/case/{a.id}/steps")
    assert resp.status_code == 200
    assert len(resp.json()) == 3
    assert resp.json()[2]["title"] == test_step_a["title"]
    assert resp.json()[1]["title"] == test_step_b["title"]
    assert resp.json()[0]["title"] == test_step_c["title"]
