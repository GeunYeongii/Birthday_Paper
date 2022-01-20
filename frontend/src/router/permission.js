import router from '@/router'

import { getAcToken } from '@/utils/auth'

// 토큰 검사 제외할 페이지
const whiteList = [
  '/',
  '/login',
  '/join'
]

router.beforeEach((to, from, next) => {
  // 작성 페이지로 들어올 경우 토큰에 관계없이 연결
  if (to.path == '/write'){
    next()
  } else {
    if (getAcToken()){
      if (whiteList.indexOf(to.path) !== -1) {
        next({ path: '/main' })
      } else {
        next()
      }
    } else {
      if (whiteList.indexOf(to.path) == -1) {
        next('/login')
      } else {
        next()
      }
    }
  }
})
