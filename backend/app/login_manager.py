from flask import jsonify, request, make_response, session, current_app
from flask_login import LoginManager
from flask import current_app
from .model.UserRepository import UserRepository

login_manager = LoginManager()
login_manager.init_app(login_manager.init_app(current_app))
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
  return UserRepository.findUserByEmail(user_id)


@login_manager.unauthorized_handler
def unauthorized():
  return make_response(jsonify(success=False), 401)


# @app.before_request
# def app_before_request():
#   if 'client_id' not in session:
#     session['client_id'] = request.environ.get(
#       'HTTP_X_REAL_IP', request.remote_addr)