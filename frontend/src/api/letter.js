import request from '@/utils/request'

export function getLetterList (params) {
  return request({
    url: '/letter/getLetterList',
    method: 'POST',
    data: params
  })
}

export function getNonMemberLetterList (params) {
  return request({
    url: '/letter/getNonMemberLetterList',
    method: 'POST',
    data: params
  })
}

export function sendMessage (params) {
  return request({
    url: '/letter/sendMessage',
    method: 'POST',
    data: params
  })
}