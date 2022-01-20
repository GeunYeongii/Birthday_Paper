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
    profile: '',
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
    SET_PROFILE: (state, profile) => {
      state.profile = profile
    },
  },

  actions: {
    Login({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        loginStart({ email: userInfo.email, pw: userInfo.pw }).then(response => {
          if (response.code == 20000) {
            const data = response.data
            commit('SET_ACTOKEN', response.accessToken)
            commit('SET_RFTOKEN', response.refreshToken)
            commit('SET_IDX', data.idx)
            commit('SET_EMAIL', data.userEmail)
            commit('SET_NICK_NAME', data.nickName)
            commit('SET_BIRTH', data.birth)
            commit('SET_PROFILE', data.profile)
            setAcToken(response.accessToken)
            setRfToken(response.refreshToken)
            resolve(response)
          } else {
            resolve(response)
          }
        }).catch(error => {
          console.log(error)
          reject(error)
        })
      }).catch(error => {
        console.log(error)
        reject(error)
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
        commit('SET_PROFILE', '')
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