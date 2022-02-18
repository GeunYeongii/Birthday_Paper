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

export function changePw (params) {
  return request({
    url: '/user/changePw',
    method: 'POST',
    data: params
  })
}

export function deleteUser (params) {
  return request({
    url: '/user/deleteUser',
    method: 'POST',
    data: params
  })
}
