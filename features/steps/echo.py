from behave import given

@given('the message "{message}"')
def step_sent_message(context, message):
    context.data["message"] = message
