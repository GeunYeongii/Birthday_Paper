import axios from 'axios'
import store from '@/store'
import { getAcToken, getRfToken } from '@/utils/auth'

const request = axios.create({
  baseURL: process.env.VUE_APP_REQUEST_URL,
  timeout: 1000 * 60 * 3,
  headers: {
    'Content-Type': 'application/json'
  }
})
// axios 모든 요청 보내기전에 수행
request.interceptors.request.use(function (config) {
  if (store.getters.rftoken) {
    config.headers.Authorization = 'Bearer ' + getAcToken()
    config.headers.rfToken = 'Bearer ' + getRfToken()
  }
  return config;
}, function (error) {
  return Promise.reject(error);
});

// axios 모든 응답 리턴전에 수행
request.interceptors.response.use(function (response) {
  return response.data;
}, function (error) {
  if (error.response.status === 401) {
    console.log('토큰 검증 실패')
  }
  return Promise.reject(error);
});

export default request
