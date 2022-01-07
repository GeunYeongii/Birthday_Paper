export function kakaoShare() {
  window.Kakao.Link.sendCustom({
    templateId: 68318,
    templateArgs: {
      'user':'test'
    }
  });
}