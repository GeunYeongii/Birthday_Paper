const getters = {
  actoken: state => state.user.actoken,
  rftoken: state => state.user.rftoken,
  idx: state => state.user.idx,
  email: state => state.user.email,
  nickname: state => state.user.nickname,
  birth: state => state.user.birth
}
export default getters
