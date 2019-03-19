from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3
import uuid
from email.utils import parseaddr
import imghdr
import os
from validate_email import validate_email
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

# configuration
DEBUG = True

# instantiate the app

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
app.config.from_object(__name__)


# enable CORS
CORS(app)

def hash_password(password):
    return pwd_context.encrypt(password)

@auth.verify_password
def verify_password(lEmail, lPassword):
    print("login email:"+lEmail)
    print("login password:"+lPassword)
    for user in USERS:
        if lEmail == user['email']:
            return pwd_context.verify(lPassword, user['password'])

USERS = [
    {
        'id': uuid.uuid4().hex,
        'username': 'admin',
        'email': 'admin@admin.com',
        'photo': 'test.jpeg',
        'password': hash_password('admin')
    }
]

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(id text, username text, email text, password text, photo text)''')
for row in c.execute('SELECT * FROM users ORDER BY username;'):
    id, username, email, password, photo = str(row).split(",")
    id = id.lstrip("(").strip("'")
    username = username.strip(" '")
    email = email.strip(" '")
    password = password.strip(" '")
    photo = photo.rstrip(")").strip(" '")
    USERS.append({'id': id, 'username': username, 'email': email, 'password': password, 'photo': photo})
conn.close()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['GET'])
def get_users():
    response_object = {'status': 'success'}
    response_object['users'] = USERS
    return jsonify(response_object)

@app.route('/login', methods=['POST'])
@auth.login_required
def login_user():
    print('Login')
    response_object = {'status': 'success'}
    response_object['message'] = 'Login successful!'
    return jsonify(response_object)


@app.route('/users', methods=['POST'])
@auth.login_required
def post_user():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    if len(post_data.get('username')) <= 256:
        if validate_email(post_data.get('email')) is True:
            for user in USERS:
                if post_data.get('email') == user['email']:
                    response_object['message'] = 'Email already exists!'
                    response_object['status'] = 'failure'
                    return jsonify(response_object)
            try:
                if imghdr.what(r''+post_data.get('photo')) is 'png' or imghdr.what(r''+post_data.get('photo')) is 'jpeg':
                    USERS.append({
                        'id': uuid.uuid4().hex,
                        'username': post_data.get('username'),
                        'email': post_data.get('email'),
                        'password': hash_password(post_data.get('password')),
                        'photo': post_data.get('photo')
                    })
                    conn = sqlite3.connect('user.db')
                    c = conn.cursor()
                    c.execute('''CREATE TABLE IF NOT EXISTS users(id text, username text, email text, password text, photo text)''')
                    c.execute("INSERT INTO users VALUES ('%s', '%s','%s','%s' ,'%s');" % (USERS[len(USERS)-1]['id'], post_data.get('username'), post_data.get('email'), hash_password(post_data.get('password')), post_data.get('photo')))
                    conn.commit()
                    conn.close()
                    response_object['message'] = 'User added!'
            except:
                response_object['message'] = 'Image is not valid!'
                response_object['status'] = 'failure'
        else:
            response_object['message'] = 'Email is not valid!'
            response_object['status'] = 'failure'
    else:
        response_object['message'] = 'Username too long!'
        response_object['status'] = 'failure'
    return jsonify(response_object)

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
#@auth.login_required
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
                try:
                    if imghdr.what(r''+post_data.get('photo')) is 'png' or imghdr.what(r''+post_data.get('photo')) is 'jpeg':
                        remove_user(user_id)
                        USERS.append({
                            'id': uuid.uuid4().hex,
                            'username': post_data.get('username'),
                            'email': post_data.get('email'),
                            'password': hash_password(post_data.get('password')),
                            'photo': post_data.get('photo')
                        })
                        conn = sqlite3.connect('user.db')
                        c = conn.cursor()
                        c.execute('''CREATE TABLE IF NOT EXISTS users(id text, username text, email text, password text, photo text)''')
                        c.execute("INSERT INTO users VALUES ('%s', '%s','%s','%s' ,'%s');" % (USERS[len(USERS)-1]['id'], post_data.get('username'), post_data.get('email'), hash_password(post_data.get('password')), post_data.get('photo')))
                        conn.commit()
                        conn.close()
                        response_object['message'] = 'User updated!'
                except:
                    response_object['message'] = 'Image is not valid!'
                    response_object['status'] = 'failure'
            else:
                response_object['message'] = 'Email is not valid!'
                response_object['status'] = 'failure'
        else:
            response_object['message'] = 'Username too long!'
            response_object['status'] = 'failure'
    if request.method == 'DELETE':
        if remove_user(user_id):
            response_object['message'] = 'User removed!'
        else:
            response_object['message'] = 'Invalid ID!'
            response_object['status'] = 'failure'
    return jsonify(response_object)

def remove_user(user_id):
    for user in USERS:
        if user['id'] == user_id:
            USERS.remove(user)
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS users(id text, username text, email text, password text, photo text)''')
            c.execute("DELETE FROM users WHERE id LIKE '%s';" % user_id)
            conn.commit()
            conn.close()
            return True
    return False


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)
