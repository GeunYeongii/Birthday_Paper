
from cgi import test


class Formatter:

  def userBasicFormating(userDetail):
    if userDetail['USER_PROFILE'] != None:
      profile = (userDetail['USER_PROFILE']).decode('UTF-8')
    else:
      profile = None

    user = {
      'idx':userDetail['IDX'],
      'userEmail':userDetail['USER_EMAIL'],
      'nickName':userDetail['NICKNAME'],
      'birth':userDetail['BIRTH'],
      'profile':profile
    }
    return user
  
  def userFormating(userDetail):
    if userDetail['USER_PROFILE'] != None:
      profile = (userDetail['USER_PROFILE']).decode('UTF-8')
    else:
      profile = None

    user = {
      'idx':userDetail['IDX'],
      'userEmail':userDetail['USER_EMAIL'],
      'pw':userDetail['USER_PW'],
      'nickName':userDetail['NICKNAME'],
      'birth':userDetail['BIRTH'],
      'profile':profile,
      'c_date':userDetail['C_DATE']
    }
    return user
  
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