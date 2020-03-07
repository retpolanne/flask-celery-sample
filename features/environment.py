from behave import fixture, use_fixture
from sample_app.factories.flask import create_app


@fixture
def app_client(context, *args, **kwargs):
    app = create_app(testing=True)
    context.client = app.test_client()
    yield context.client


def before_feature(context, feature):
    use_fixture(app_client, context)


def before_scenario(context, feature):
    context.data = {}
