from .conftest import test_case_a


def test_create_test_case(client, db_with_3_suites):
    a, b, c = db_with_3_suites
    resp = client.post(f"/suite/{a.id}/case", json=test_case_a)

    assert resp.status_code == 200
    assert resp.json()["title"] == test_case_a["title"]
    assert resp.json()["desc"] == test_case_a["desc"]
    assert resp.json()["id"]
    assert resp.json()["suite_id"] == a.id


def test_get_suite_test_cases(client, db_with_3_suites, db_with_3_cases):
    a, b, c = db_with_3_suites
    resp = client.get(f"/suite/{a.id}/cases")
    assert resp.status_code == 200
    assert len(resp.json()) == 3


def test_delete_test_case(client, db_with_3_cases):
    a, b, c = db_with_3_cases
    resp = client.delete(f"/case/{a.id}")
    assert resp.status_code == 200
    resp = client.get(f"/case/{a.id}")
    assert resp.status_code == 404


def test_update_test_case(client, db_with_3_cases):
    a, b, c = db_with_3_cases
    resp = client.patch(f"/case/{a.id}", json={"title": "Test Case AAA"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Case AAA"
    resp = client.get(f"/case/{a.id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Test Case AAA"
