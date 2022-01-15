import request from '@/utils/request'

export function getLetterList (params) {
  return request({
    url: '/letter/getLetterList',
    method: 'POST',
    data: params
  })
}