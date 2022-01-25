from flask import Blueprint, jsonify, request

from ..model.CardRepository import CardRepository
from ..common.Message import Message

myPage = Blueprint("myPage", __name__, url_prefix="/myPage")

@myPage.route("/getHistoryList", methods=['POST'])
def getHistoryList():
  print('== getHistoryListStart ==')
  try:
    request_data = request.get_json()
    userIdx = request_data['idx']

    statisticsList = CardRepository.findCardByStatisticsYear(userIdx)
    
    Result = { 'code' : 20000, 'data' : statisticsList }
    return jsonify(Result)

  except Exception as e:
    print(e)
    Result = { 'code' : 50000, 'message' : Message.Letter.noneCard.value }
    return jsonify(Result)
