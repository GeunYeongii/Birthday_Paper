import Cookies from 'vue-cookies'

const acsTk = 'accessToken'

export function getToken () {
  return Cookies.get(acsTk);
}

export function setToken (token) {
  return Cookies.set(acsTk, token);
}

export function removeToken () {
  return Cookies.remove(acsTk);
}
