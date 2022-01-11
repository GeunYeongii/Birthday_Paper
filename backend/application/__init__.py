from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask import Flask, jsonify, request, render_template, make_response, session, current_app
from flask_cors import CORS
from . import main
from .api_test import test
from .control.user_mgmt import User
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)
app.secret_key = 'cky0935'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


app.register_blueprint(main.main)
app.register_blueprint(test.test)



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


@app.before_request
def app_before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get(
            'HTTP_X_REAL_IP', request.remote_addr)