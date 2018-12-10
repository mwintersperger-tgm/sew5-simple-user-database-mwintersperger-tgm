import pytest
import flask

from src.main.python.server import app as App
from src.main.python.server import createDB

@pytest.fixture
def app():
    app = App
    return app

@pytest.fixture
def db():
    db = createDB
    return db

def test_ping(app):
    res = app.get('/ping')
    assert res.status_code == 200

def test_app_ping(app):
    res = app.get('/ping')
    assert res.json == {'pong!'}
