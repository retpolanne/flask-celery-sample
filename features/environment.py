from behave import fixture, use_fixture
from sample_app import create_app


@fixture
def app_client(context, *args, **kwargs):
    app = create_app()
    app.config['TESTING'] = True
    context.client = app.test_client()
    yield context.client


def before_feature(context, feature):
    use_fixture(app_client, context)


def before_scenario(context, feature):
    context.data = {}
