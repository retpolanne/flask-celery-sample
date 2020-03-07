import json


def send_mail(flask_client, email_address, message):
    return flask_client.post(
        "/echo/send-mail", 
        data=json.dumps(
            {
                "message": message,
                "email_address": email_address
            }),
        headers={
            "Content-Type": "application/json"
        }
    )


def test_send_mail(flask_client):
    message = "hello world"
    email = "foobar@helloworld.io"
    res = send_mail(flask_client, message, email)
    assert res.status_code == 201
