from flask_jwt_extended import ( jwt_required, create_access_token, get_jwt_identity, create_refresh_token )
from flask import jsonify, request
from functools import wraps

import datetime

class JwtService:
  def createAccessToken(userEmail):
    delta = datetime.timedelta(hours = 1)
    access_token = create_access_token(identity = userEmail, expires_delta = delta)
    return access_token
  
  def createRefreshToken(userEmail):
    delta = datetime.timedelta(days = 14)
    refresh_token = create_refresh_token(identity = userEmail, expires_delta = delta)
    return refresh_token
  
  # Token 유효성 검사
  def checkJwtRequired(f):
    @wraps(f)
    @jwt_required()
    def checkJwt(*args, **kwargs):
      userEmail = get_jwt_identity()
      return f(userEmail, *args, **kwargs)

    return checkJwt