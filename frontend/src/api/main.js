import request from '@/utils/request'

export function main() {
  return request({
    url: '/',
    method: 'post'
  })
}

export function test1() {
  return request({
    url: '/test1',
    method: 'post'
  })
}

export function test2() {
  return request({
    url: '/test2',
    method: 'post'
  })
}

export function test3(params) {
  return request({
    url: '/test3',
    method: 'post',
    data: params
  })
}