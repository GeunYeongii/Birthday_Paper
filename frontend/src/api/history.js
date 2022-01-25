import request from '@/utils/request'

export function getHistoryList (params) {
  return request({
    url: '/myPage/getHistoryList',
    method: 'POST',
    data: params
  })
}