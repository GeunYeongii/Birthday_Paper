from flask import jsonify, request
from flask import Blueprint
from flask.helpers import make_response

test = Blueprint("test", __name__, url_prefix="/test")

@test.route("/test1", methods=['POST'])
def test1():
  data = request.get_json()
  print('test2 페이지 테스트')
  return jsonify('test1 테스트 성공')

@test.route("/test2", methods=['POST'])
def test2():
  data = request.get_json()
  print('test2 페이지 테스트')
  return jsonify('test2 테스트 성공')

# 데이터 받을 경우
@test.route("/test3", methods=['POST'])
def test3():
  # request 사용해서 post 데이터 사용
  print(request.get_json())
  print('params 테스트')
  return jsonify('test3 테스트 성공')

