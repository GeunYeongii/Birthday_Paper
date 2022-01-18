from enum import Enum

class Message:
  class Login(Enum):
    success = '로그인에 성공하였습니다'
    noneUser = '없는 유저 입니다'
    differentPasswords = '비밀번호가 다릅니다'
    error = '로그인에 실패하였습니다.'

  class SignUp(Enum):
    success = '회원가입에 성공하였습니다'
    noneUser = '이메일이 중복되었습니다'
    error = '회원가입에 실패하였습니다.'
