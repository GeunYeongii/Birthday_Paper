from tabnanny import check
from flask import Blueprint, jsonify, request
import hashlib, base64

from sympy import EX

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
@user.route("/password_change", methods=['POST'])
def password_change():
  print('== password Changing ==')
  try :
    # request_data = request.get_json()
    # userEmail = request_data['email']
    # userPw = request_data['pw']
    
    # 예외 처리들은 아직 안함. 나중에 할 예정
    userEmail = request.form.get('email')
    userPw = hash_password(request.form.get('pw'))
    new_password = hash_password(request.form.get('new_pw'))
    
    # 밑에 코드는 둘 실제값이 같아도 해시값은 다르게 나옴. -> 시크릿코드를 적용해야함.
    # hash를 bcrypt hash 라이브러리를 쓰거나 hash_password 함수 수정할 예정
    print(userPw.encode().decode('utf-8'),new_password.encode().decode('utf-8'))
    
    if check_password(userPw,new_password) is False :
      UserRepository.update(userEmail,new_password)
      print(userPw is new_password)
      Result = { 'code' : 20000, 'message' : Message.changePw.success.value }
    else :
      Result = { 'code' : 50000, 'message' : Message.changePw.samePasswords.value }
      
    return jsonify(Result)
  
  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.changePw.error.value }
    return jsonify(Result)
  
# Delete User
@user.route("/delete_user", methods=['POST'])
def delete_user():
  print("== delete User ==")
  try :
    userEmail = request.form.get('email')
    userPw = request.form.get('pw')
    
    user = UserRepository.findUserByEmail(userEmail)
    
    if user is not None :
      UserRepository.delete(userEmail)
      Reuslt = { 'code' : 20000, 'message' : Message.deleteUser.success.value }
    else :
      Result = { 'code' : 50000, 'message' : Message.deleteUser.wrongInfo.value }
      
    return jsonify(Result)
  
  except Exception as e:
    print(e)
    Reuslt = { 'code' : 50000, 'message' : Message.deleteUser.error.value }
    return jsonify(Result)
  

# Password to hash
def hash_password(userPw):
  m = hashlib.sha256()
  m.update(userPw.encode('utf-8'))
  return m.hexdigest()

# check hash Password
def check_password(userPw, checkPw):
  #print(userPw.decode('utf-8'),checkPw.decode('utf-8'))
  return hash_password(userPw) == checkPw