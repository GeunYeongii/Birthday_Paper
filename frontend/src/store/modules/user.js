/* eslint-disable */
import { loginStart } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'

const user = {
  state: {
    token: getToken(),
    idx: '',
    email: '',
    nickname: '',
    birth: '',
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_IDX: (state, idx) => {
      state.idx = idx
    },
    SET_EMAIL: (state, email) => {
      state.email = email
    },
    SET_NICK_NAME: (state, nickname) => {
      state.nickname = nickname
    },
    SET_BIRTH: (state, birth) => {
      state.birth = birth
    },
  },

  actions: {
    Login({ commit }, userInfo) {
      return new Promise((resolve) => {
        loginStart({ email: userInfo.email, pw: userInfo.pw }).then(response => {
          if (response.code == 20000) {
            const data = response.data
            commit('SET_TOKEN', response.Authorization)
            commit('SET_IDX', data.IDX)
            commit('SET_EMAIL', data.USER_EMAIL)
            commit('SET_NICK_NAME', data.NICKNAME)
            commit('SET_BIRTH', data.BIRTH)
            resolve()
          } else {
            console.error('로그인 실패', response.message)
          }
        }).catch(error => {
          console.error(error)
        })
      }).catch(error => {
        console.error(error)
      })
    },
    LogOut({ commit, state }) {
      return new Promise((resolve) => {
        commit('SET_TOKEN', '')
        commit('SET_IDX', '')
        commit('SET_EMAIL', '')
        commit('SET_NICK_NAME', '')
        commit('SET_BIRTH', '')
        removeToken()
        resolve()
      })
    },
  }
}

export default user