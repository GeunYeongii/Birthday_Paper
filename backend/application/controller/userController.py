from flask import jsonify, request
from flask import Blueprint
from ..common.user_mgmt import User

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/joinStart", methods=['POST'])
def joinStart():
  try:
    request_data = request.get_json()
    print('joinStart params :: ', request_data)

    id = request_data['id']
    pw = request_data['pw']
    nickNm = request_data['nickNm']
    birth = request_data['birth']
    profileImg = request_data['profileImg']
    
    User.create(id, pw, nickNm, birth, profileImg)
    
    
    data = { 'code' : 20000 }
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)

@user.route("/loginStart", methods=['POST'])
def loginStart():
  try:
    request_data = request.get_json()
    print('loginStart params :: ', request_data)
    
    id = request_data['id']
    pw = request_data['pw']
    
    data = { 'code' : 20000 }
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)
