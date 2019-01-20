import os
import tempfile

import pytest

from src.main.python.server import app as App
from src.main.python.server import createDB

@pytest.fixture
def client():
    App.app.config['TESTING'] = True
    client = App.app.test_client()

    yield client

@pytest.fixture
def db():
    db = createDB
    yield db

def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200

def test_app_ping(client):
    res = client.get('/ping')
    assert res.json == {'pong!'}


