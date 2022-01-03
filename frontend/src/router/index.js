import { createWebHistory, createRouter } from 'vue-router';

const routes = [
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
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});