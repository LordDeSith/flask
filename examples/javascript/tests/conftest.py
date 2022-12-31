import pytest

from js_example import app
from flask.app_testing import AppTestingUtil

@pytest.fixture(name="app")
def fixture_app():
    app.testing = True
    yield app
    app.testing = False


@pytest.fixture
def client(app):
    return AppTestingUtil(app).test_client()
