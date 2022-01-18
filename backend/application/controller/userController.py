from flask import jsonify, request
from flask import Blueprint
from ..common.UserMgmt import UserMgmt
from ..common.Message import Message
import hashlib, datetime
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, create_refresh_token, 
    jwt_refresh_token_required
)

user = Blueprint("user", __name__, url_prefix="/user")

# JoinStart
@user.route("/joinStart", methods=['POST'])
def joinStart():
  print('== joinStart ==')
  try:
    request_data = request.get_json()
    userEmail = request_data['email']
    userPw = request_data['pw']
    nickName = request_data['nickNm']
    birth = request_data['birth']
    profileImg = request_data['profileImg']

    user = UserMgmt.findUserEmail(userEmail)

    if user is None:
      userPw = hash_password(userPw)
      UserMgmt.create(userEmail, userPw, nickName, birth, profileImg)
      Result = { 'code' : 20000, 'message' : Message.SignUp.success.value }
    else:
      Result = { 'code' : 50000, 'message' : Message.SignUp.noneUser.value }

    return jsonify(Result)

  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.SignUp.error.value }
    return jsonify(Result)

# loginStart
@user.route("/loginStart", methods=['POST'])
def loginStart():
  print('== loginStart ==')
  try:
    request_data = request.get_json()
    userEmail = request_data['email']
    userPw = request_data['pw']


    user = UserMgmt.findUserEmail(userEmail)
    if user is not None:
      if check_password(userPw, user['USER_PW']):

        delta = datetime.timedelta(days = 1)
        access_token = create_access_token(identity = user['USER_EMAIL'], expires_delta = delta)
        # refresh_token = create_refresh_token(identity = user['USER_EMAIL'], expires_delta = delta)

        Result = { 
          'code' : 20000,
          'message' : Message.Login.success.value,
          'data' : user,
          'access_token' : access_token }
      else:
        Result = { 'code' : 50000, 'message' : Message.Login.differentPasswords.value }
    else:
      Result = { 'code' : 50000, 'message' : Message.Login.noneUser.value }

    return jsonify(Result)

  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.Login.error.value }
    return jsonify(Result)

# Password to hash
def hash_password(userPw):
  m = hashlib.sha256()
  m.update(userPw.encode('utf-8'))
  return m.hexdigest()

# check hash Password
def check_password(userPw, checkPw):
  return hash_password(userPw) == checkPw


# 헤더로 수신된 Access 토큰 유효성 검사 후 서명된 사용자 찾기
@user.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# 하루짜리 토큰 발급
@user.route('/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token, current_user=current_user)