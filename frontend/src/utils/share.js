export function kakaoShare() {
  window.Kakao.Link.sendCustom({
    templateId: 68318,
    templateArgs: {
      'title': '제목 영역입니다.',
      'description': '설명 영역입니다.'
    }
  });
}