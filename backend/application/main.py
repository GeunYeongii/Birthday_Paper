from flask import jsonify, request
from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/", methods=['POST'])
def index():
  print('Rest API 테스트')
  return jsonify('Rest API 테스트')

@main.route("/test1", methods=['POST'])
def test1():
  print('test1 페이지 테스트')
  return jsonify('test1 페이지 테스트')

@main.route("/test2", methods=['POST'])
def test2():
  print('test2 페이지 테스트')
  return jsonify('test2 페이지 테스트')

# 데이터 받을 경우
@main.route("/test3", methods=['POST'])
def test3():
  # request 사용해서 post 데이터 사용
  print(request.get_json())
  print('params 테스트')
  return jsonify('params 테스트 성공')
