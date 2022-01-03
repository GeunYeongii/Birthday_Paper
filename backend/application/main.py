from flask import jsonify
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
