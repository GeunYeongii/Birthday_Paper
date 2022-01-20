
class Formatter:

  def userBasicFormating(userDetail):
    user = {
      'idx':userDetail['IDX'],
      'userEmail':userDetail['USER_EMAIL'],
      'nickName':userDetail['NICKNAME'],
      'birth':userDetail['BIRTH'],
      'profile':userDetail['USER_PROFILE']
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