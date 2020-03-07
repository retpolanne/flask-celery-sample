def healthcheck(flask_client):
    return flask_client.get("/healthcheck")


def test_healthcheck(flask_client):
    res = healthcheck(flask_client)
    assert res.status_code == 200
    assert "ok" in res.json.get("message")
