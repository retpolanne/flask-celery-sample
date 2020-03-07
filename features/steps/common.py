import json
from behave import when, then


@given('the message "{message}"')
def step_sent_message(context, message):
    context.data["message"] = message


@when('I make a {verb} to "{endpoint}"')
def step_verb_impl(context, verb, endpoint):
    if verb == "get":
        context.response = context.client.get(endpoint)
    if verb == "post":
        context.response = context.client.post(
            endpoint,
            data=json.dumps(context.data),
            headers={"Content-Type": "application/json"}
        )


@then('the status code should be {status_code}')
def step_status_code_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('there should be a message saying "{message}"')
def step_check_response_message(context, message):
    res = json.loads(context.response.data)
    assert res.get("message") == message
