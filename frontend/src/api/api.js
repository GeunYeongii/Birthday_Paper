import request from '@/utils/request'

export function test (params) {
  return request({
    url: '/test/test1',
    method: 'post',
    data: params
  })
}