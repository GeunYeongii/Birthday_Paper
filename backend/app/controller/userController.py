from lib2to3.pgen2 import token
from argon2 import hash_password
from flask import jsonify, request, make_response
from flask import Blueprint
import uuid
import joblib
from sympy import re
from werkzeug.security import generate_password_hash, check_password_hash
from ..model import User
from app import db
import jwt,datetime,app
from functools import wraps

user = Blueprint("user", __name__, url_prefix="/user")

# Token 데코레이터 만들어둠
def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    
    if 'x-access-token' in request.headers :
      token = request.headers['x-access-token']
    if not token :
      return jsonify({'message' : 'Token is missing!'}),401
    try:
      data = jwt.decode(token, app.config['SECRETE_KEY'])
      current_user = User.query.filter_by(public_id=data['public_id']).first()
    except:
      return jsonify({'message' : 'Token is invalid!'}), 401
    
    return f(current_user, *args, **kwargs)
  
  return decorated



@user.route('/',method=['GET'])
@token_required
def get_all_users(current_user):
      
  if not current_user.admin :
    return jsonify({'message' : 'Cannot perform that function!'})
  users = User.query.all()
  output = []
    
  for user in users :
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    output.append(user_data)
    
  return jsonify({'users': output})

@user.route('/<public_id>',method=['GET'])
@token_required
def get_one_user(current_user,public_id):
  if not current_user.admin :
    return jsonify({'message' : 'Cannot perform that function!'})
  user = User.query.filter_by(public_id=public_id).first()
  
  if not user:
    return jsonify({'message' : 'No user found!'})
  
  user_data = {}
  user_data['public_id'] = user.public_id
  user_data['username'] = user.username
  user_data['password'] = user.password
  user_data['admin'] = user.admin
  
  return jsonify({'user' : user_data})

@user.route('/',method=['POST'])
@token_required
def create_user(current_user):
  if not current_user.admin :
    return jsonify({'message' : 'Cannot perform that function!'})
  data = request.get_json()
  hash_password = generate_password_hash(data['password'],method='sha256')
  
  new_user = User(public_id=str(uuid.uuid4()),name=data['username'],password=hash_password,admin=False)
  db.session.add(new_user)
  db.session.commit()
  
  return jsonify({'code' : 20000, 'message' : 'New user created!'})

@user.route('/<public_id>',method=['PUT'])
@token_required
def promote_user(current_user,public_id):
  if not current_user.admin :
    return jsonify({'message' : 'Cannot perform that function!'})
  user = User.query.filter_by(public_id=public_id).first()
  
  if not user:
    return jsonify({'message' : 'No user found!'})    

  user.admin = True
  db.session.commit()
   
  return jsonify({'message' : 'The user has been promoted'})

@user.route('/<public_id>',method=['DELETE'])
@token_required
def delete_user(current_user, public_id):
  if not current_user.admin :
    return jsonify({'message' : 'Cannot perform that function!'})
  user = User.query.filter_by(public_id=public_id).first()
  
  if not user:
    return jsonify({'message' : 'No user found!'})
  db.session.delete(user)
  db.session.commit()
  
  return jsonify({'message' : 'The user has been deleted'})

@user.route('/login>')
def login():
  auth = request.authorization
  
  if not auth or not auth.username or not auth.password:
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
  
  user = User.query.filter_by(name=auth.username).first()
  if not user :
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
  
  if check_password_hash(user.password, auth.password) :
    token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SCRETE-KEY'])
    
    return jsonify({'token' : token.decode('UTF-8')})
  
  return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})










# 예닮이
#---------------------------------------------------------
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
