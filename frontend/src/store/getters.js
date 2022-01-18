const getters = {
  token: state => state.user.token,
  idx: state => state.user.idx,
  email: state => state.user.email,
  nickname: state => state.user.nickname,
  birth: state => state.user.birth
}
export default getters
