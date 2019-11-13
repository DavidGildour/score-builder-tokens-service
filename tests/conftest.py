import pytest

from app import app


@pytest.fixture(scope='module')
def client():
    """ Testing client for the tokens service """
    app.config.from_object('config.TestingConfig')

    return app.test_client()