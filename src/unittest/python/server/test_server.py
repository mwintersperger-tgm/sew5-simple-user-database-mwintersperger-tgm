import os
import tempfile
import json
import pytest
import uuid

from flask import Response

from src.main.python.server.app import app as App

@pytest.fixture
def app():
    app = App
    return app

# Sanity Tests

def test_ping_code(client):
    res = client.get('/ping')
    assert res.status_code == 200

def test_ping_return(client):
    res = client.get('/ping')
    assert res.json == 'pong!'

# Post Method

def test_post_valid_status(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'success'

def test_post_valid_message(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'User added!'

def test_post_valid_code(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_username_status(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_email_status(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_photo_status(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'bla.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_username_message(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'Username too long!'

def test_post_invalid_email_message(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'Email is not valid!'

def test_post_invalid_photo_message(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'bla.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'Image is not valid!'

def test_post_invalid_username_code(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_email_code(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_photo_code(client):
    data = {
        'id': uuid.uuid4().hex,
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'bla.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

# Get Method

def test_get_code(client):
    res = client.get('/users')
    assert res.status_code == 200

def test_get_status_Message(client):
    res = client.get('/users')
    assert res.json['status'] == 'success'

#def test_get_response(client):
#    res = client.get('/users')
#    assert res.json['users'] == '[]'
