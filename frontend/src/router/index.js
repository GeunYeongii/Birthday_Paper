import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const route = [
  {
    path: '/',
    name: 'Intro',
    component: () => import('@/views/intro/index'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index'),
  },
  {
    path: '/join',
    name: 'Join',
    component: () => import('@/views/join/index'),
  },
  {
    path: '/main',
    name: 'Main',
    component: () => import('@/views/main/index'),
  },
  {
    path: '/write',
    name: 'Write',
    component: () => import('@/views/write/index'),
  },
  {
    path: '/notice',
    name: 'Notice',
    component: () => import('@/views/notice/index'),
  },
]

export default new Router({
  mode: 'history',
  routes: route
})


