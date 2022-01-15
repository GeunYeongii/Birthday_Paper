import request from '@/utils/request'

export function joinStart (params) {
  return request({
    url: '/user/joinStart',
    method: 'POST',
    data: params
  })
}

export function loginStart (params) {
  return request({
    url: '/user/loginStart',
    method: 'POST',
    data: params
  })
}