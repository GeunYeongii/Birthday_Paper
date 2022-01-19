import Cookies from 'vue-cookies'

const acToken = 'accessToken'
const rfToken = 'refreshToken'

export function getAcToken () {
  return Cookies.get(acToken);
}

export function setAcToken (token) {
  return Cookies.set(acToken, token);
}

export function removeAcToken () {
  return Cookies.remove(acToken);
}

export function getRfToken () {
  return Cookies.get(rfToken);
}

export function setRfToken (token) {
  return Cookies.set(rfToken, token);
}

export function removeRfToken () {
  return Cookies.remove(rfToken);
}
