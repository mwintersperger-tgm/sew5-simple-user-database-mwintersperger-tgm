import os
import tempfile
import json
import pytest

from flask import Response

#from src.main.python.server.app import app as App

"""

@pytest.fixture(autouse=True)
def app():
    app = App
    yield app

# Sanity Tests

def test_ping_code(client):
    res = client.get('/ping')
    assert res.status_code == 200

def test_ping_return(client):
    res = client.get('/ping')
    assert res.json == 'pong!'

# Post Method

def test_post_valid_status(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'success'

def test_post_valid_message(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'User added!'

def test_post_valid_code(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_username_status(client):
    data = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_email_status(client):
    data = {
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_photo_status(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'bla.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['status'] == 'failure'

def test_post_invalid_username_message(client):
    data = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'Username too long!'

def test_post_invalid_email_message(client):
    data = {
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.json['message'] == 'Email is not valid!'

#def test_post_invalid_photo_message(client):
#    data = {
#        'username': 'Michael',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'bla.jpeg'
#    }
#    url = '/users'
#    res = client.post(url, json=data)
#    assert res.json['message'] == 'Image is not valid!'

def test_post_invalid_username_code(client):
    data = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_email_code(client):
    data = {
        'username': 'Michael',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    res = client.post(url, json=data)
    assert res.status_code == 200

def test_post_invalid_photo_code(client):
    data = {
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

def test_get_status(client):
    res = client.get('/users')
    assert res.json['status'] == 'success'

def test_get_response_username(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    res = client.get('/users')
    dict = json.loads(str(res.json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    assert dict["username"] == 'Michael'

def test_get_response_email(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    res = client.get('/users')
    dict = json.loads(str(res.json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    assert dict["email"] == 'mwintersperger@student.tgm.ac.at'

def test_get_response_photo(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    res = client.get('/users')
    dict = json.loads(str(res.json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    assert dict["photo"] == 'test.jpeg'

# Delete Method

def test_delete(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    client.delete("/users/%s" % dict["id"])
    assert str(client.get("/users").json["users"]) == "[]"

def test_delete_status(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    res = client.delete("/users/%s" % dict["id"])
    assert res.json['status'] == 'success'

def test_delete_message(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    res = client.delete("/users/%s" % dict["id"])
    assert res.json['message'] == 'User removed!'

def test_delete_code(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
    res = client.delete("/users/%s" % dict["id"])
    assert res.status_code == 200

def test_delete_invalidID_status(client):

    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    res = client.delete("/users/%s" % "abc")
    assert res.json['status'] == 'failure'

def test_delete_invalidID_message(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)
    client.delete("/users/%s" % "abc")
    res = client.delete("/users/%s" % "abc")
    assert res.json['message'] == 'Invalid ID!'

# Put Method

def test_put_valid_status(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['status'] == 'success'

def test_put_valid_message(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['message'] == 'User updated!'

def test_put_valid_code(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.status_code == 200

def test_put_invalid_username_status(client):
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['status'] == 'failure'

def test_put_invalid_email_status(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['status'] == 'failure'

#def test_put_invalid_photo_status(client):
#    for user in client.get("/users").json["users"]:
#        client.delete("/users/%s" % user["id"])
#    data = {
#        'username': 'Michael',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'test.jpeg'
#    }
#    url = '/users'
#    client.post(url, json=data)
#
#    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
#
#    data2 = {
#        'username': 'Michael2',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'bla.jpeg'
#    }
#    url2 = '/users/%s' % dict["id"]
#
#    res = client.put(url2, json=data2)
#    assert res.json['status'] == 'failure'

def test_put_invalid_username_message(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['message'] == 'Username too long!'

def test_put_invalid_email_message(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.json['message'] == 'Email is not valid!'

#def test_put_invalid_photo_message(client):
#    for user in client.get("/users").json["users"]:
#        client.delete("/users/%s" % user["id"])
#    data = {
#        'username': 'Michael',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'test.jpeg'
#    }
#    url = '/users'
#    client.post(url, json=data)
#
#    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
#
#    data2 = {
#        'username': 'Michael2',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'bla.jpeg'
#    }
#    url2 = '/users/%s' % dict["id"]
#
#    res = client.put(url2, json=data2)
#    assert res.json['message'] == 'Image is not valid!'

def test_put_invalid_username_code(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.status_code == 200

def test_put_invalid_email_code(client):
    for user in client.get("/users").json["users"]:
        client.delete("/users/%s" % user["id"])
    data = {
        'username': 'Michael',
        'email': 'mwintersperger@student.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url = '/users'
    client.post(url, json=data)

    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))

    data2 = {
        'username': 'Michael2',
        'email': 'mwinterspergerstudent.tgm.ac.at',
        'photo': 'test.jpeg'
    }
    url2 = '/users/%s' % dict["id"]

    res = client.put(url2, json=data2)
    assert res.status_code == 200

#def test_put_invalid_photo_code(client):
#    for user in client.get("/users").json["users"]:
#        client.delete("/users/%s" % user["id"])
#    data = {
#        'username': 'Michael',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'test.jpeg'
#    }
#    url = '/users'
#    client.post(url, json=data)
#
#    dict = json.loads(str(client.get("/users").json["users"]).lstrip("[").rstrip("]").replace("'", "\""))
#
#    data2 = {
#        'username': 'Michael2',
#        'email': 'mwintersperger@student.tgm.ac.at',
#        'photo': 'bla.jpeg'
#    }
#    url2 = '/users/%s' % dict["id"]
#
#    res = client.put(url2, json=data2)
#    assert res.status_code == 200

"""
