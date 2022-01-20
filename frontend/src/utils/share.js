export function kakaoShare(data) {
  window.Kakao.Link.sendCustom({
    templateId: 68318,
    templateArgs: {
      'nickname':data.nickname,
      'userIdx':data.userIdx
    }
  });
}