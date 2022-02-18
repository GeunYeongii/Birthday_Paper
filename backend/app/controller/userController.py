from tabnanny import check
from tkinter import FALSE
from flask import Blueprint, jsonify, request
import base64, bcrypt

from ..model.UserRepository import UserRepository
from ..common.JwtService import JwtService
from ..common.Formatter import Formatter
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
      hashedPassword = hash_password(userPw).decode('utf-8')
      
      # 이미지 바이너리화 후 저장
      img_binary = None
      if len(profileImg) != 0:
        img_data = profileImg[0].read()
        img_binary = base64.b64encode(img_data)
        img_binary = img_binary.decode('UTF-8')

      UserRepository.create(userEmail, hashedPassword, nickName, birth, img_binary)
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
    print(user)
    if user is not None:
      if bcrypt.checkpw(userPw.encode('utf-8'),user['USER_PW'].encode('utf-8')) :
        access_token = JwtService.createAccessToken(user['USER_EMAIL'])
        refresh_token = JwtService.createRefreshToken(user['USER_EMAIL'])

        Result = { 
          'code' : 20000,
          'message' : Message.Login.success.value,
          'data' : Formatter.userFormating(user),
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


# change Password
@user.route("/changePw", methods=['POST'])
def changePw():
  userPw = request.form.get('pw')
  newPassword = request.form.get('new_pw')
  
  #user = UserRepository.findUserByEmail(userEmail)
  print('== password Changing ==')
  try :
    if bcrypt.checkpw(hash_password(userPw),user['USER_PW'].encode('utf-8')) :
      Result = { 'code' : 50000, 'message' : Message.changePw.wrongPw.value}
    elif userPw != newPassword :
      newPassword = hash_password(newPassword).decode('utf-8')
      #UserRepository.update(userEmail,newPassword)
      Result = { 'code' : 20000, 'message' : Message.changePw.success.value }
    else :
      Result = { 'code' : 50000, 'message' : Message.changePw.samePasswords.value }
      
    return jsonify(Result)
  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.changePw.error.value }
    return jsonify(Result)
  
  
# Delete User
@user.route("/deleteUser", methods=['POST'])
def deleteUser():
  print("== delete User ==")
  try :
    userEmail = request.form.get('email')
    userPw = request.form.get('pw')
    
    user = UserRepository.findUserByEmail(userEmail)
    
    print(user)
    if user is not None :
      UserRepository.delete(userEmail)
      Result = { 'code' : 20000, 'message' : Message.deleteUser.success.value }
    else :
      Result = { 'code' : 50000, 'message' : Message.deleteUser.wrongInfo.value }
      
    return jsonify(Result)
  
  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.deleteUser.error.value }
    return jsonify(Result)
  
# Password to hash
def hash_password(userPw):
  return bcrypt.hashpw(userPw.encode('utf-8'),bcrypt.gensalt())