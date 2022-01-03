import request from '@/utils/request'

export function main () {
    return request({
      url: '/',
      method: 'post'
    })
  }