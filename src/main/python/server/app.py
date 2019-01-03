from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import uuid
from email.utils import parseaddr
import imghdr
import os
from validate_email import validate_email


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

USERS = [
]
conn = sqlite3.connect('user.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM users ORDER BY username;'):
    id, username, email, photo = str(row).split(",")
    id = id.lstrip("(").strip("'")
    username = username.strip(" '")
    email = email.strip(" '")
    photo = photo.rstrip(")").strip(" '")
    USERS.append({'id': id, 'username': username, 'email': email, 'photo': photo})
conn.close()
# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/users', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if len(post_data.get('username')) <= 256:
            if validate_email(post_data.get('email')) is True:
                for user in USERS:
                    if post_data.get('email') == user['email']:
                        response_object['message'] = 'Email already exists!'
                        response_object['status'] = 'failure'
                        return jsonify(response_object)
                if imghdr.what(r''+post_data.get('photo')) is 'png' or imghdr.what(r''+post_data.get('photo')) is 'jpeg':
                    USERS.append({
                        'id': uuid.uuid4().hex,
                        'username': post_data.get('username'),
                        'email': post_data.get('email'),
                        'photo': post_data.get('photo')
                    })
                    conn = sqlite3.connect('user.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO users VALUES ('%s', '%s','%s','%s');" % (USERS[len(USERS)-1]['id'], post_data.get('username'), post_data.get('email'), post_data.get('photo')))
                    conn.commit()
                    conn.close()
                    response_object['message'] = 'User added!'
                else:
                    response_object['message'] = 'Image not valid!'
                    response_object['status'] = 'failure'
            else:
                response_object['message'] = 'Email is not valid!'
                response_object['status'] = 'failure'
        else:
            response_object['message'] = 'Username too long!'
            response_object['status'] = 'failure'
    else:
        response_object['users'] = USERS
    return jsonify(response_object)

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
def single_user(user_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        if len(post_data.get('username')) <= 256:
            if validate_email(post_data.get('email')) is True:
                for user in USERS:
                    if user_id != user['id']:
                        if post_data.get('email') == user['email']:
                            response_object['message'] = 'Email already exists!'
                            response_object['status'] = 'failure'
                            return jsonify(response_object)
                if imghdr.what(r''+post_data.get('photo')) is 'png' or imghdr.what(r''+post_data.get('photo')) is 'jpeg':
                    remove_user(user_id)
                    USERS.append({
                        'id': uuid.uuid4().hex,
                        'username': post_data.get('username'),
                        'email': post_data.get('email'),
                        'photo': post_data.get('photo')
                    })
                    conn = sqlite3.connect('user.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO users VALUES ('%s', '%s','%s','%s');" % (USERS[len(USERS)-1]['id'], post_data.get('username'), post_data.get('email'), post_data.get('photo')))
                    conn.commit()
                    conn.close()
                    response_object['message'] = 'User updated!'
                else:
                    response_object['message'] = 'Image not valid!'
                    response_object['status'] = 'failure'
            else:
                response_object['message'] = 'Email is not valid!'
                response_object['status'] = 'failure'
        else:
            response_object['message'] = 'Username too long!'
            response_object['status'] = 'failure'
    if request.method == 'DELETE':
        remove_user(user_id)
        response_object['message'] = 'User removed!'
    return jsonify(response_object)

def remove_user(user_id):
    for user in USERS:
        if user['id'] == user_id:
            USERS.remove(user)
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            c.execute("DELETE FROM users WHERE id LIKE '%s';" % user_id)
            conn.commit()
            conn.close()
            return True
    return False

if __name__ == '__main__':
    app.run()
