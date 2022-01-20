import router from '@/router'

import { getAcToken } from '@/utils/auth'

// 토큰 검사 제외할 페이지
const whiteList = [
  '/',
  '/login',
  '/join',
]

router.beforeEach((to, from, next) => {
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
})
