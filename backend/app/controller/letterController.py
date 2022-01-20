from flask import Blueprint, jsonify, request
import math

from ..model.UserRepository import UserRepository
from ..model.CardRepository import CardRepository
from ..common.JwtService import JwtService
from ..common.Formatter import Formatter
from ..common.Message import Message

letter = Blueprint("letter", __name__, url_prefix="/letter")

@letter.route("/getLetterList", methods=['POST'])
@JwtService.checkJwtRequired
def getLetterList(user=None, token=None):
  print('== getLetterListStart ==')
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
              card = Formatter.cardFormating(cardList[count])
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


@letter.route("/getNonMemberLetterList", methods=['POST'])
def getNonMemberLetterList():
  print('== getNonMemberLetterListStart ==')
  try:
    request_data = request.get_json()
    userIdx = request_data['userIdx']

    user = UserRepository.findUserByIdx(userIdx)
    cardList = CardRepository.findCardByReceiverIdx(userIdx)

    totalCount = len(cardList)
    totalPage = math.ceil(len(cardList)/8)
        
    count = 0
    letterList = []
    for i in range(totalPage):
      list = []
      for j in range(8):
        if count < totalCount:
          card = Formatter.cardFormating(cardList[count])
          list.append(card)
          count += 1
      letterList.append(list)

    data = {
      'data' : { 'letterList': letterList, "totalCount": totalCount, "totalPage": totalPage, "receiver": Formatter.userBasicFormating(user) },
      'code' : 20000
    }
    
  except Exception as e:
    data = {
      'code' : 50000,
      'message' : Message.Letter.noneCard
    }
  
  return jsonify(data)


@letter.route("/sendMessage", methods=['POST'])
def sendMessage():
  print('== sendMessageStart ==')
  try:
    request_data = request.get_json()
    receiver = request_data['receiver']
    sendParams = request_data['sendParams']

    data = {
      'code' : 20000,
      'message' : '성공'
    }

  except Exception as e:
    data = {
      'code' : 50000,
      'message' : e
    }
  
  return jsonify(data)