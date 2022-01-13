import re
from flask import jsonify, request
from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/main", methods=['POST'])
def load_user():
  data = {'user_email' : "test@gmail.com"}
  return data
  # return jsonify({
  #   'user_email' : data['user_email']
  # })
  
  # ,
  #   'user_pw' : data['user_pw'],
  #   'user_nickName' : data['user_nickName'],  
  #   'user_birth' : data['user_birth'],
  #   'user_profile' : data['user_profile']
