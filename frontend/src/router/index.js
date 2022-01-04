import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const route = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/main/index'),
  },
  {
    path: '/test1',
    name: 'test1',
    component: () => import('@/views/test/test1'),
  },
  {
    path: '/test2',
    name: 'test2',
    component: () => import('@/views/test/test2'),
  },
]

export default new Router({
  mode: 'history',
  routes: route
})


