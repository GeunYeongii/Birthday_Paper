from flask import Blueprint, jsonify, request
import hashlib, base64

from ..model.UserRepository import UserRepository
from ..common.JwtService import JwtService
from ..common.Message import Message

user = Blueprint("user", __name__, url_prefix="/user")

# JoinStart
@user.route("/joinStart", methods=['POST'])
def joinStart():
  print('== joinStart ==')
  try:
    userEmail = request.form.get('email')
    userPw = request.form.get('pw')
    nickName = request.form.get('nickNm')
    birth = request.form.get('birth')
    profileImg = request.files.getlist("file[]")

    user = UserRepository.findUserByEmail(userEmail)

    if user is None:
      userPw = hash_password(userPw)
    
      # 이미지 바이너리화 후 저장
      img_binary = None
      if len(profileImg) != 0:
        img_data = profileImg[0].read()
        img_binary = base64.b64encode(img_data)
        img_binary = img_binary.decode('UTF-8')

      UserRepository.create(userEmail, userPw, nickName, birth, img_binary)
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

    user = UserRepository.findUserByEmail(userEmail)
    if user is not None:
      if check_password(userPw, user['USER_PW']):

        access_token = JwtService.createAccessToken(user['USER_EMAIL'])
        refresh_token = JwtService.createRefreshToken(user['USER_EMAIL'])

        Result = { 
          'code' : 20000,
          'message' : Message.Login.success.value,
          'data' : user,
          'accessToken' : access_token,
          'refreshToken' : refresh_token }
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