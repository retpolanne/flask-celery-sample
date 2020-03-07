import json

def echo(flask_client, message):
    return flask_client.post(
        "/echo/send-message", 
        data=json.dumps({"message": message}),
        headers={
            "Content-Type": "application/json"
        }
    )


def test_echo(flask_client):
    message = "hello world"
    res = echo(flask_client, message)
    assert res.status_code == 200
    assert message in res.json.get("message")
