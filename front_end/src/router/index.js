import Vue from 'vue'
import Router from 'vue-router'

import Navbar from '@/components/Navbar.vue'

import Registrarse from '@/components/Registrarse.vue'
import ListaProductos from '@/components/ListaProductos.vue'
import Cartas from '@/components/Cartas.vue'
import Home from '@/components/Home.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/login',
      name: 'login',
      component: Registrarse
    },
    {
      path: '/producto',
      name: 'producto',
      component: ListaProductos
    },
    {
      path: '/cartas',
      name: 'cartas',
      component: Cartas
    }
  
  ],
  mode: 'history'
})
