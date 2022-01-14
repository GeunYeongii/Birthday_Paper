import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const route = [
  // 로그인 정보가 있으면 main으로 리다이렉트 
  { path: '/', name: 'Intro', component: () => import('@/views/intro/index') },
  { path: '/join', name: 'join', component: () => import('@/views/join/index') },
  { path: '/login', name: 'login', component: () => import('@/views/login/index') },
  { path: '/notice', name: 'notice', component: () => import('@/views/notice/index') },
  { path: '/main', name: 'main', component: () => import('@/views/main/index') },
  { path: '/write', name: 'write', component: () => import('@/views/write/index') },
  { path: '/myPage', name: 'myPage', component: () => import('@/views/myPage/index') },
  { path: '/introduce', name: 'introduce', component: () => import('@/views/introduce/index') },
]

export default new Router({
  mode: 'history',
  routes: route
})
