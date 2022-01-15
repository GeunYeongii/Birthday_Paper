export function kakaoShare(data) {
  window.Kakao.Link.sendCustom({
    templateId: 68318,
    templateArgs: {
      'user':data.user
    }
  });
}