import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Exhauster from "../views/Exhauster";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/:id',
    name: 'Exhauster',
    component: Exhauster,
    props: true,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
