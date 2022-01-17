from datetime import datetime
from tkinter.messagebox import NO
from flask_login import UserMixin
from ..model.mysql import conn_mysqldb
import logging


class User(UserMixin):

    def __init__(self, user_email, user_pw,user_nickName,user_birth,user_profile):
        self.id = user_email
        self.pw = user_pw
        self.user_nickName = user_nickName
        self.user_birth = user_birth
        self.user_profile = user_profile
        
    def get_id(self):
        return str(self.user_email)

    @staticmethod
    def get(user_email):
      try:
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + str(user_email) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()

        return user

      except Exception as e:
        logging.error(e)

    @staticmethod
    def create(user_email, user_pw,user_nickName,user_birth,user_profile=None):
      try:
        user = User.get(user_email)
        print(user is None)
        if user == None:

          # TODO 비밀번호 해쉬화 로직 추가

          mysql_db = conn_mysqldb()
          db_cursor = mysql_db.cursor()
          sql = "INSERT INTO user_info (USER_EMAIL, USER_PW, NICKNAME, BIRTH) VALUES ('%s', '%s', '%s', '%s')" % (
              str(user_email), str(user_pw),str(user_nickName),str(user_birth))
          db_cursor.execute(sql)
          mysql_db.commit()
          return True
        else:
          return False
      except Exception as e:
        logging.error(e)
        return False

    @staticmethod
    def delete(user_email):
      try:
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_email)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted
      except Exception as e:
        logging.error(e)
        return False
