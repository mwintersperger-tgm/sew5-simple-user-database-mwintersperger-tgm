import pytest

from src.main.python.server import app as App

@pytest.fixture
def app():
    app = App
    return app

def test_ping(app):
    res = app.get('/ping')
    assert res.status_code == 200
