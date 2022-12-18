from yatmos import __version__


def test_read_root(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["version"] == __version__
