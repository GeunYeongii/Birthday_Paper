import Vue from 'vue'
import Router from 'vue-router'
import header from '@/views/layout/header'

Vue.use(Router)

const route = [
  {
    path: '/',
    name: 'Intro',
    component: () => import('@/views/intro/index'),
  },
  {
    path: '/',
    component: header,
    children: [
      { path: '/login', component: () => import('@/views/login/index'), hidden: true },
      { path: '/join', component: () => import('@/views/join/index'), hidden: true },
      { path: '/main', component: () => import('@/views/main/index'), hidden: true },
      { path: '/write', component: () => import('@/views/write/index'), hidden: true },
      { path: '/notice', component: () => import('@/views/notice/index'), hidden: true },
    ]
  },
]

export default new Router({
  mode: 'history',
  routes: route
})


