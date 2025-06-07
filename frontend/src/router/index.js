import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login.vue'
import Register from '../views/Register.vue'
import Home from '../views/Home.vue'
import PersonalInfo from '../views/PersonalInfo.vue'
import store from '../store'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/home', component: Home },
  { path: '/person', component: PersonalInfo },
  {
    path: '/tripform',
    name: 'TripForm',
    component: () => import('@/views/TripForm.vue')
  },
  {
    path: '/tripdetail',
    name: 'TripDetail',
    component: () => import('@/views/TripDetail.vue')
  },
  {
    path: '/orderlist',
    name: 'OrderList',
    component: () => import('@/views/OrderList.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 简单路由守卫示例
router.beforeEach(async (to, from, next) => {
  const isAuthenticated = store.state.isAuthenticated
  if (to.meta.requiresAuth && !isAuthenticated) {
    try {
      await store.dispatch('fetchUserInfo')
      next()
    } catch (error) {
      next('/login')
    }
  } else if ((to.path === '/login' || to.path === '/register') && isAuthenticated) {
    next('/home')
  } else {
    next()
  }
})
export default router
