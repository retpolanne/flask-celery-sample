from behave import given


@given('the email address "{email_address}"')
def step_email_address(context, email_address):
    context.data["email_address"] = email_address


@then('the task "{task}" should be scheduled')
def step_check_task_scheduled(context, task):
    pass
