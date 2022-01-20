from flask import jsonify
from flask import Blueprint
import math

from ..model.CardRepository import CardRepository
from ..common.JwtService import JwtService
from ..common.Message import Message

letter = Blueprint("letter", __name__, url_prefix="/letter")

@letter.route("/getLetterList", methods=['POST'])
@JwtService.checkJwtRequired
def getLetterList(user=None, token=None):
  try:
    if user :
      try:
        cardList = CardRepository.findCardByReceiverIdx(user['IDX'])

        totalCount = len(cardList)
        totalPage = math.ceil(len(cardList)/8)
        
        count = 0
        letterList = []
        for i in range(totalPage):
          list = []
          for j in range(8):
            if count < totalCount:
              card = cardFormating(cardList[count])
              list.append(card)
              count += 1
          letterList.append(list)

        data = {
          'data' : { 'letterList': letterList, "totalCount": totalCount, "totalPage": totalPage },
          'code' : 20000,
          'token' : token
        }
      except Exception as e:
        data = {
          'code' : 50000,
          'message' : Message.Letter.noneCard
        }
    else:
      data = {
        'code' : 50000,
        'message' : Message.Token.expiredToken
      }
    return jsonify(data)

  except Exception as e:
    print(e)
    data = { 'code' : 50000 }
    return jsonify(data)


def cardFormating(cardDetail):
  card = {
    'idx':cardDetail['IDX'],
    'senderNm':cardDetail['SENDER_NM'],
    'receiverNm':cardDetail['RECEIVER_NM'],
    'receiverIdx':cardDetail['RECEIVER_IDX'],
    'letterContent':cardDetail['CARD_MSG'],
    'c_date':cardDetail['C_DATE']
  }
  return card

