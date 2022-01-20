from flask_login import UserMixin
from .DbModule import Database

class CardRepository(UserMixin):

  def __init__(self, sender_nm, receiver_nm, receiver_idx, card_msg, c_date):
    self.sender_nm = sender_nm
    self.receiver_nm = receiver_nm
    self.receiver_idx = receiver_idx
    self.card_msg = card_msg
    self.c_date = c_date

  @staticmethod
  def findCardByReceiverIdx(userIdx):
    print('== card_data findCardByReceiverIdx ==')
    try:
      db_class = Database()
      sql = "SELECT * FROM card_data WHERE RECEIVER_IDX = '" + str(userIdx) + "'"
      cardList = db_class.executeAll(sql)
      return cardList
    except Exception as e:
      print(e)
