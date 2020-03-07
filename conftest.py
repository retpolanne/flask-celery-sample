import pytest

from sample_app import create_app

@pytest.fixture(scope="module")
def flask_client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
