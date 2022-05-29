import os
import pathlib
import flask
from flask import Flask, request, url_for, session, abort, redirect
from authlib.integrations.flask_client import OAuth
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


port=5001

# App config
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Session config
app.secret_key = '4325bedae2c4e7e790c43a05bc14d1914a979f9e07d92236ac93ec9533899fad'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='881072346550-btb1pupabk29t35tcbkejdgh4or62tk8.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(80), unique=True, nullable=False)
    markDone = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(300))

    # db.create_all()

    def __repr__(self):
        return f"{self.id}, {self.taskName}, {self.markDone} - {self.description}"


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500))

    def __repr__(self):
        return f"{self.id}, {self.token}"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        tokenValue=None
        paramToken=''
        paramToken=request.args.get('access_token', None)
        if 'Authorization' in request.headers:
            tokenValue = request.headers['Authorization']
            tokenValue = tokenValue.replace('Bearer ', '')
        print(f"tokenValue from header: {tokenValue}")
        print(f"tokenValue from parm: {paramToken}")
#        user = dict(session).get('profile', None)
        myToken = dict(session).get('access_token', None)
        result = Token.query.filter_by(id=1).first()
        if (result.token == tokenValue):
            print(f"header Has access! token: {result.token}\n")
            return f(*args, **kwargs)
        elif (result.token == myToken):
            print(f"session Has access! token: {result.token}\n")
            return f(*args, **kwargs)
        elif (result.token == paramToken):
            print(f"Param Has access! token: {result.token}\n")
            return f(*args, **kwargs)
        else:
            print(f"No access! token: {result.token}\n")
        # return 'You aint logged in, no page for u!'
        # return redirect('/login')
        return "Todo List, need to login <a href='/login'><button>Login</button></a>"
    return decorated_function


@app.route('/todo')
@login_required
def get_todos():
    todos = Todo.query.all()
    if todos is None:
        return {"error": "No data found"}
    output = []
    for todo in todos:
        if todo is None:
            return {"error": "No data found"}
        todo_data = {'id': todo.id, 'taskName': todo.taskName, 'markDone': todo.markDone, 'description': todo.description}
        output.append(todo_data)
    return f"todos: {output} \
        <br> <a href='/logout'><button>logout</button></a>"


@app.route('/todo/<id>')
@login_required
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return { "id": todo.id, "taskName": todo.taskName, "markDone": todo.markDone, "description": todo.description}


@app.route('/todo', methods=['POST'])
@login_required
def add_todo():
    todo = Todo(taskName=request.json['taskName'], markDone=request.json['markDone'], description=request.json['description'])
    db.session.add(todo)
    db.session.commit()
    return {'id': todo.id}


@app.route('/todo/<id>', methods=['DELETE'])
@login_required
def delete_todo(id):
    todo = Todo.query.get(id)
    if todo is None:
        return {"error": "not found"}
    db.session.delete(todo)
    db.session.commit()
    return {'message': "Done delete todo!"}


@app.route('/todo_complete/<id>', methods=['POST'])
@login_required
def complete_todo(id):
    result = Todo.query.filter_by(id=id).first()
    if not result:
        return {'message': "List doesn't exist, cannot update"}
    result.markDone = True
    db.session.commit()
    return {'message': "Marking done!", 'id': result.id}


@app.route('/welcome')
@login_required
def welcome():
    return f"Hello, you are logged in! \
        <br> <a href='/todo'><button>List Todo List</button></a> \
        <br> <a href='/logout'><button>logout</button></a>"


@app.route('/')
@login_required
def hello_world():
    if "profile" in session:
        email = dict(session)['profile']['email']
        return f"Hello, you are logged in as {email}! \
        <br> <a href='/todo'><button>List Todo List</button></a> \
        <br> <a href='/logout'><button>logout</button></a>"
    else:
        print("rerouting...")
        return f"Hello, please login first! \
        <br> <a href='/login'><button>login</button></a>"


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    access_token = google.authorize_access_token()  # Access token from google (needed to get user info)
    print (f"{access_token['access_token']}")
    result = Token.query.filter_by(id=1).first()
    myToken = ''
    if not result:
        myToken = Token(token=access_token['access_token'])
        db.session.add(myToken)
        print(f"no result, added!\n")
    else:
        print(f"old access: {result.token}")
        result.token = access_token['access_token']
        myToken = result.token
        print(f"renewing token")
        print(f"current access: {result.token}")
    db.session.commit()
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session['access_token'] = myToken
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/welcome')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    result = Token.query.filter_by(id=1).first()
    if result:
        result.token = ""
        print(f"clearing token")
        db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    print(f"hello world!\n")
    app.run(host="0.0.0.0", port=port, debug=True)