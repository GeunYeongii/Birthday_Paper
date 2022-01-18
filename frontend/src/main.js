import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import store from '@/store'
import vuetify from './plugins/vuetify'
import VueCookies from "vue-cookies";
import { mdiBullhornOutline } from '@mdi/js';
// 공통으로 사용하는 컴포넌트
import alert from '@/components/alert'
import spinner from '@/components/spinner'
import '@/router/permission'

import '@/assets/css/main.css'

Vue.config.productionTip = false
// 공통으로 사용하는 컴포넌트 등록
Vue.component('s-alert', alert)
Vue.component('s-spinner', spinner)

Vue.use(VueCookies);
//쿠키의 만료일 7일 (글로벌 세팅)
Vue.$cookies.config("7d");

new Vue({
  vuetify,
  store,
  router: router,
  mdiBullhornOutline,
  render: h => h(App)
}).$mount('#app')