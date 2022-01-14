from flask import jsonify, request
from flask import Blueprint
from flask.helpers import make_response

letter = Blueprint("letter", __name__, url_prefix="/letter")

@letter.route("/getLetterList", methods=['POST'])
def getLetterList():
  try:
    request_data = request.get_json()
    userIdx = request_data['userIdx']

    # 받은 user idx 값으로 user 데이터 조회
    # user 데이터로 card_data 에서 해당 user가 받은 card list 조회
    
    data = {
      'data' : {
        'letterList': [
          [
            { 'idx': 0, 'userNm': "test1", 'imgUrl': '@/assets/img/asset_4.png' },
            { 'idx': 1, 'userNm': "test2", 'imgUrl': '@/assets/img/asset_3.png' },
            { 'idx': 2, 'userNm': "test3", 'imgUrl': '@/assets/img/asset_2.png' },
            { 'idx': 3, 'userNm': "test4", 'imgUrl': '@/assets/img/asset_1.png' },
            { 'idx': 4, 'userNm': "test5", 'imgUrl': '@/assets/img/asset_1.png' },
            { 'idx': 5, 'userNm': "test6", 'imgUrl': '@/assets/img/asset_2.png' },
            { 'idx': 6, 'userNm': "test7", 'imgUrl': '@/assets/img/asset_4.png' },
            { 'idx': 7, 'userNm': "test8", 'imgUrl': '@/assets/img/asset_3.png' }
          ],[
            { 'idx': 8, 'userNm': "test9", 'imgUrl': '@/assets/img/asset_4.png' },
            { 'idx': 9, 'userNm': "test10", 'imgUrl': '@/assets/img/asset_3.png' },
            { 'idx': 10, 'userNm': "test11", 'imgUrl': '@/assets/img/asset_2.png' },
            { 'idx': 11, 'userNm': "test12", 'imgUrl': '@/assets/img/asset_1.png' },
            { 'idx': 12, 'userNm': "test13", 'imgUrl': '@/assets/img/asset_1.png' },
            { 'idx': 13, 'userNm': "test14", 'imgUrl': '@/assets/img/asset_2.png' },
            { 'idx': 14, 'userNm': "test15", 'imgUrl': '@/assets/img/asset_4.png' },
            { 'idx': 15, 'userNm': "test16", 'imgUrl': '@/assets/img/asset_3.png' }
          ],[
            { 'idx': 16, 'userNm': "test17", 'imgUrl': '@/assets/img/asset_4.png' },
            { 'idx': 17, 'userNm': "test18", 'imgUrl': '@/assets/img/asset_3.png' },
            { 'idx': 18, 'userNm': "test19", 'imgUrl': '@/assets/img/asset_2.png' },
            { 'idx': 19, 'userNm': "test20", 'imgUrl': '@/assets/img/asset_1.png' }
          ]
        ],
        "totalCount": 20,
        "totalPage": 3
      },
      'code' : 20000
    }
    
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)
