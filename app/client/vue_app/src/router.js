import Vue from 'vue'
import Router from 'vue-router'
import Devhelp from './views/Devhelp.vue'
import Api from './views/Api.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'api',
      component: Api
    },
    {
      path: '/devhelp',
      name: 'devhelp',
      component: Devhelp
    }
  ]
})
