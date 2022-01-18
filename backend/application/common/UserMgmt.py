from flask_login import UserMixin
from ..model.dbModule import Database

class UserMgmt(UserMixin):

  @staticmethod
  def findUserEmail(userEmail):
    print('== user_info findUserEmail ==')
    try:
      db_class = Database()
      sql = "SELECT * FROM bp_user_info WHERE USER_EMAIL = '" + str(userEmail) + "'"
      user = db_class.executeOne(sql)
      return dict(user)
    except Exception as e:
      print(e)

  @staticmethod
  def create(userEmail, userPw, nickName, birth, profileImg):
    print('== user_info create ==')
    try:
      db_class = Database()
      sql = "INSERT INTO bp_user_info (USER_EMAIL, USER_PW, NICKNAME, BIRTH) VALUES ('%s', '%s', '%s', '%s')" % (
        str(userEmail), str(userPw), str(nickName), str(birth))
      db_class.execute(sql)
      db_class.commit()
    except Exception as e:
      print(e)