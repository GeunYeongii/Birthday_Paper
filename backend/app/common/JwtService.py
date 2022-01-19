from ..model.UserRepository import UserRepository

from datetime import datetime, timedelta
from flask import jsonify, request
from functools import wraps

import jwt, datetime

class JwtService:
  def createAccessToken(userEmail):
    payload = {'userEmail': userEmail, 'exp': datetime.datetime.utcnow() +timedelta(seconds=5)}
    access_token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256")
    return access_token
  
  def createRefreshToken(userEmail):
    payload = {'userEmail': userEmail, 'exp': datetime.datetime.utcnow() +timedelta(minutes=1)}
    refresh_token = jwt.encode(payload, "SECRET_KEY", algorithm="HS256")
    return refresh_token
  
  def checkToken(token):
    try:
      decodeToken = jwt.decode(token, "SECRET_KEY", algorithms='HS256')
      user = UserRepository.findUserByEmail(decodeToken['userEmail'])
      return user
    except Exception as e:
      print(e)
      return None

  # Token 유효성 검사
  def checkJwtRequired(f):
    @wraps(f)
    def checkJwt(*args, **kwargs):
      if 'Access-Token' in request.headers:
        access_token = request.headers['Access-Token']
        atuser = JwtService.checkToken(access_token)
      if 'Refresh-Token' in request.headers:
        refresh_token = request.headers['Refresh-Token']
        rtuser = JwtService.checkToken(refresh_token)

      if atuser:
        user = atuser
        token = None
      elif rtuser:
        user = rtuser
        token = JwtService.createAccessToken(user['USER_EMAIL'])
      else:
        user = None
        token = None

      return f(user, token, *args, **kwargs)

    return checkJwt