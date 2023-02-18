import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    jwt: localStorage.getItem("token"),
    refreshJwt: localStorage.getItem("refresh_token"),
    backendUrl: "wss://localhost/api",
    webSocketUrl: "wss://localhost:8001"
  },

  mutations: {
    updateToken(state, newToken) {
      // Записывается во время авторизации либо во время обновления токена
      localStorage.setItem("token", newToken);
      state.jwt = newToken;
    },
    updateRefreshToken(state, newToken) {
      // Записывается во время авторизации
      localStorage.setItem("refresh_token", newToken);
      state.refreshJwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem("token");
      localStorage.removeItem("refresh_token");
      state.jwt = null;
      state.refreshJwt = null;
      state.isAuthenticated = false;
    },
  },

  actions: {
  },

  modules: {
  },

  getters: {
    getServerUrl: state => {
      return state.backendUrl
    },
    getJWT: state => {
      return state.jwt
    },
    getRefreshJWT: state => {
      return state.refreshJwt
    },
    getRefreshStatus: state => {
      return state.refreshStatus
    },
    getIsAuthenticated: state => {
      return state.isAuthenticated
    },
    getAuthUser: state => {
      return state.authUser
    },
    getProfileInfo: state => {
      return state.profileInfo
    },
  },

  plugins: [createPersistedState()]
})
