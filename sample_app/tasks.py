from sample_app.factories.celery import make_celery
from sample_app.factories.flask import create_app
from sample_app.controllers.foobar import foobar

celery = make_celery(create_app())


@celery.task
def send_email(email_address, message):
    return foobar(email_address, message)
