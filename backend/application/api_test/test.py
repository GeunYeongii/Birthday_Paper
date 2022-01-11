from flask import jsonify, request
from flask import Blueprint

test = Blueprint("test", __name__, url_prefix="/test")

@test.route("/test1", methods=['POST'])
def test1():
  print('test1 페이지 테스트')
  return jsonify({
    'data' : 'api',
    'string' : 'test!!'
  })


@test.route("/test2", methods=['POST'])
def test2():
  print('test2 페이지 테스트')
  return jsonify('test2 페이지 테스트')

# 데이터 받을 경우
@test.route("/test3", methods=['POST'])
def test3():
  # request 사용해서 post 데이터 사용
  print(request.get_json())
  print('params 테스트')
  return jsonify('params 테스트 성공')

