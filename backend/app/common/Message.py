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
  
  class Letter(Enum):
    successSend = '카드를 보내는데 성공하였습니다.'
    errorSend = '카드를 보내는데 실패하였습니다.\n잠시후 다시 시도해 주세요.'
    noneCard = '카드정보를 불러오지 못하였습니다. 잠시후 다시 시도해 주세요.'

  class Token(Enum):
    expiredToken = '로그인 정보가 만료되었습니다. 다시 로그인 해주세요'
