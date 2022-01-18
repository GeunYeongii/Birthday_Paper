import router from '@/router'
import store from '@/store'

// 토큰 검사 제외할 페이지
const whiteList = [
  '/',
  '/login',
  '/join',
]

router.beforeEach((to, from, next) => {
  if (store.getters.token) {
    if (whiteList.indexOf(to.path) !== -1) {
      next('/main')
    } else {
      next()
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      if (store.getters.token) {
        next()
      } else {
        next('/login')
      }
    }
  }
})
