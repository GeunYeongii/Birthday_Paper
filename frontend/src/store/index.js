import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

import user from './modules/user'
import getters from './getters'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    user,
  },
  getters,
  plugins: [
    createPersistedState({ paths: ["user"] })
  ]
})

export default store
