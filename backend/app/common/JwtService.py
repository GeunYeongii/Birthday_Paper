import datetime
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies, create_refresh_token)

class JwtService:
  def createAccessToken(userEmail):
    delta = datetime.timedelta(hours = 1)
    access_token = create_access_token(identity = userEmail, expires_delta = delta)
    return access_token
  
  def createRefreshToken(userEmail):
    delta = datetime.timedelta(days = 14)
    refresh_token = create_refresh_token(identity = userEmail, expires_delta = delta)
    return refresh_token

  # 헤더로 수신된 Access 토큰 유효성 검사 후 서명된 사용자 찾기
  # @user.route('/protected', methods=['GET'])
  # @jwt_required
  # def protected():
  #   current_user = get_jwt_identity()
  #   return jsonify(logged_in_as=current_user), 200


  # 하루짜리 토큰 발급
  # @user.route('/refresh', methods=['GET'])
  # @jwt_refresh_token_required
  # def refresh():
  #   current_user = get_jwt_identity()
  #   access_token = create_access_token(identity=current_user)
  #   return jsonify(access_token=access_token, current_user=current_user)