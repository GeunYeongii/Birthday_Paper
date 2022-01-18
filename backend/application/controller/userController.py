from flask import jsonify, request
from flask import Blueprint
from ..common.UserMgmt import UserMgmt
from ..common.Message import Message
import hashlib

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
        Result = { 'code' : 20000, 'message' : Message.Login.success.value }
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
