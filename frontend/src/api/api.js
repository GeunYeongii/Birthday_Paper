import request from '@/utils/request'

export function test (params) {
  return request({
    url: '/test',
    method: 'post',
    data: params
  })
}