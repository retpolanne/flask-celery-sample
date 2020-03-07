from unittest.mock import patch
from sample_app.tasks import send_email


def test_send_email():
    with patch('sample_app.tasks.foobar') as foobar_patch:
        send_email("foobar@helloworld.io", "hello world")
        foobar_patch.assert_called_once_with(
            "foobar@helloworld.io", "hello world")
