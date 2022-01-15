import request from '@/utils/request'

export function joinStart (params) {
  return request({
    url: '/join/joinStart',
    method: 'POST',
    data: params
  })
}