import Vue from 'vue'
import Router from 'vue-router'


import Registrarse from '@/components/Registrarse.vue'
import ListaProductos from '@/components/ListaProductos.vue'
import Cartas from '@/components/Cartas.vue'
import Home from '@/components/Home.vue'
import Profile from '@/components/Profile.vue'
import login from '@/components/login.vue'
import Details from '@/components/Details.vue'
import Vender from '@/components/Vender.vue'
import Busqueda from '@/components/Busqueda.vue'
import Pruebahome from '@/components/Pruebahome.vue'
import Carrito from '@/components/Carrito.vue'
import Footer from '@/components/Footer.vue'




Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
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
    },
    {
      path: '/r',
      name: 'r',
      component: Registrarse
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },{
    path: '/Details',
    name: 'Details',
    component: Details
    },{
      path: '/Vende',
      name: 'vende',
      component: Vender
    },
    {
      path: '/busqueda',
      name: 'busqueda',
      component: Busqueda
    },{
    path: '/nuevo',
    name: 'nuevo',
    component: Pruebahome
  },
  {
    path: '/carrito',
    name:'carrito',
    component: Carrito
},
{
  path: '/foo',
  name: 'foo',
  component: Footer
},
{
  path: '/test',
  name: 'test',
  component: Pruebahome
}
  ],
  mode: 'history'
})
