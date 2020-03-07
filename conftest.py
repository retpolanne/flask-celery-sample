import pytest

from sample_app.factories.flask import create_app

@pytest.fixture(scope="module")
def flask_client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


@pytest.fixture(scope='module')
def celery_config():
    return {
        'broker_url': 'redis://',
        'result_backend': 'redis://'
    }
