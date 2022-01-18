from flask import jsonify, request
from flask import Blueprint
from ..common.UserMgmt import UserMgmt

letter = Blueprint("letter", __name__, url_prefix="/letter")

@letter.route("/getLetterList", methods=['POST'])
def getLetterList():
  try:
    request_data = request.get_json()
    userIdx = request_data['userIdx']

    # [TODO] 데이터 베이스 서버 오픈되면 실 데이터 주고 받는거 테스트 해야함
    # 받은 user idx 값으로 user 데이터 조회
    # user 데이터로 card_data 에서 해당 user가 받은 card list 조회 
    
    data = {
      'data' : {
        'letterList': [
          [
            { 'idx': 0, 'userNm': "예닮", 'letterContent': '1월9일\n생일\n진심으로\n축하해!' },
            { 'idx': 1, 'userNm': "근영", 'letterContent': '생일축하하고!!\n 항상 행복한 하루 보내길 바래♥' },
            { 'idx': 2, 'userNm': "test3", 'letterContent': '너랑 모든 순간이 행복했고, 함께해준 너에게 항상 고마워 :)' },
            { 'idx': 3, 'userNm': "YD", 'letterContent': '오늘은 맛있는것도 많이 먹고,\n 좋은 사람들과 즐거운 시간 보내면서\n누구보다 행복했으면 좋겠다.' },
            { 'idx': 4, 'userNm': "훈제족발", 'letterContent': '너를 언제나 응원하고 있어!' },
            { 'idx': 5, 'userNm': "HunJeJogBal", 'letterContent': '안녕! 난 HunJeJogBal 이라고해!' },
            { 'idx': 6, 'userNm': "Gnyiii", 'letterContent': 'Gnyiii 의 깃헙에 놀러와 주세요!' },
            { 'idx': 7, 'userNm': "GeunYeong", 'letterContent': '안녕! 난 GeunYeong 이라고해!' }
          ],[
            { 'idx': 8, 'userNm': "관악요정", 'letterContent': '여러분 ~ 모두 관악구로 와주세요 !' },
            { 'idx': 9, 'userNm': "광주내려갈럼", 'letterContent': '광주에 내려가서 놀려고 했는데 말이지!\n 실패를 해버렸지 뭐얌! >< 빠끄' },
            { 'idx': 10, 'userNm': "복치학우", 'letterContent': '복치학우 .. 공부... ㅎ...하자' },
            { 'idx': 11, 'userNm': "생강 싫은 진저 쿠키", 'letterContent': '진저 쿠피는 생강이 진짜 너무너무 싫어' },
            { 'idx': 12, 'userNm': "금요일은 커피머신 청소", 'letterContent': '근영씨! \n금요일에는 커피머신 청소좀 안 까먹고 해주셨으면 좋겠어요 ㅎㅎ ^^' },
            { 'idx': 13, 'userNm': "코로나19", 'letterContent': '코로나 19는 2019년 부터 시작되었으며 ... ' },
            { 'idx': 14, 'userNm': "눈누냔냐", 'letterContent': '노는게 제일 좋아 ~~ 친구들 모여라 ~!' },
            { 'idx': 15, 'userNm': "이직중독자", 'letterContent': '이제 입사 1개월찬데 이직마렵다...' }
          ],[
            { 'idx': 16, 'userNm': "14년 지기", 'letterContent': '14년 지기는 이런거 안한다.' },
            { 'idx': 17, 'userNm': "붕알친구", 'letterContent': '너랑 친구한지가 벌써\n 10년이 넘은거 같은데....' },
            { 'idx': 18, 'userNm': "태릉주민", 'letterContent': '태릉주민태릉주민\n태릉주민태릉주민' },
            { 'idx': 19, 'userNm': "파주에살지롱", 'letterContent': '난 파주에 살고 있는 \n\n이예닮 이다!' }
          ]
        ],
        "totalCount": 20,
        "totalPage": 3
      },
      'code' : 20000
    }
    
    # for page in data['data']['letterList'] :
    #   for List in page :
    #     List['letterContent'].replace('안녕','시발') 

    
    
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)
