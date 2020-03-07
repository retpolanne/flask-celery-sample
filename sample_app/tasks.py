from sample_app.factories.celery import make_celery
from sample_app.factories.flask import create_app

celery = make_celery(create_app())


def foobar(email_address, message):
    return "foobar"

@celery.task
def send_email(email_address, message):
    return foobar(email_address, message)
