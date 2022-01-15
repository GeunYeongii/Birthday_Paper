from flask import jsonify, request
from flask import Blueprint

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/joinStart", methods=['POST'])
def joinStart():
  try:
    request_data = request.get_json()
    id = request_data['id']
    pw = request_data['pw']
    nickNm = request_data['nickNm']
    birth = request_data['birth']
    profileImg = request_data['profileImg']
    
    print('id',id)
    print('pw',pw)
    print('nickNm',nickNm)
    print('birth',birth)
    print('profileImg',profileImg)
    
    data = { 'code' : 20000 }
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)
