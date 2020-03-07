import json
from unittest.mock import patch


def echo(flask_client, message):
    return flask_client.post(
        "/echo/send-message",
        data=json.dumps({"message": message}),
        headers={
            "Content-Type": "application/json"
        }
    )


def send_email(flask_client, email_address, message):
    return flask_client.post(
        "/echo/send-email",
        data=json.dumps(
            {
                "message": message,
                "email_address": email_address
            }),
        headers={
            "Content-Type": "application/json"
        }
    )


def test_echo(flask_client):
    message = "hello world"
    res = echo(flask_client, message)
    assert res.status_code == 200
    assert message in res.json.get("message")


def test_send_mail(flask_client):
    message = "hello world"
    email = "foobar@helloworld.io"
    with patch('celery.Celery.send_task') as send_task:
        res = send_email(flask_client, email, message)
        send_task.assert_called_once_with(
            'tasks.send_email', args=[email, message])
    assert res.status_code == 201
