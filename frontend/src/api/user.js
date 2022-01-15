import request from '@/utils/request'

export function joinStart (params) {
  return request({
    url: '/user/joinStart',
    method: 'POST',
    data: params
  })
}