from flask import jsonify
from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/", methods=['POST'])
def index():
  print('Rest API 테스트')
  return jsonify('Rest API 테스트')
