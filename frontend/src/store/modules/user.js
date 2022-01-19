/* eslint-disable */
import { loginStart } from '@/api/user'
import { getAcToken, setAcToken, removeAcToken, getRfToken, setRfToken, removeRfToken } from '@/utils/auth'

const user = {
  state: {
    actoken: getAcToken(),
    rftoken: getRfToken(),
    idx: '',
    email: '',
    nickname: '',
    birth: '',
  },

  mutations: {
    SET_ACTOKEN: (state, actoken) => {
      state.actoken = actoken
    },
    SET_RFTOKEN: (state, rftoken) => {
      state.rftoken = rftoken
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
            commit('SET_ACTOKEN', response.accessToken)
            commit('SET_RFTOKEN', response.refreshToken)
            commit('SET_IDX', data.IDX)
            commit('SET_EMAIL', data.USER_EMAIL)
            commit('SET_NICK_NAME', data.NICKNAME)
            commit('SET_BIRTH', data.BIRTH)
            setAcToken(response.accessToken)
            setRfToken(response.refreshToken)
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
        commit('SET_ACTOKEN', '')
        commit('SET_RFTOKEN', '')
        commit('SET_IDX', '')
        commit('SET_EMAIL', '')
        commit('SET_NICK_NAME', '')
        commit('SET_BIRTH', '')
        removeAcToken()
        removeRfToken()
        resolve()
      })
    },
    RefreshActoken({ commit }, actoken){
      return new Promise((resolve) => {
        commit('SET_ACTOKEN', '')
        commit('SET_ACTOKEN', actoken)
        setAcToken(actoken)
        resolve()
      })
    }
  }
}

export default user