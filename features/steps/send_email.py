from behave import given
from unittest.mock import patch


@given('the email address "{email_address}"')
def step_email_address(context, email_address):
    context.data["email_address"] = email_address
    context.send_task = patch('celery.Celery.send_task')
