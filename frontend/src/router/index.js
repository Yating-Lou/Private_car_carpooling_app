import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/trip/form',
    name: 'TripForm',
    component: () => import('@/views/TripForm.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/trip/list',
    name: 'TripList',
    component: () => import('@/views/TripList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/order/list',
    name: 'OrderList',
    component: () => import('@/views/OrderList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/personal/info',
    name: 'PersonalInfo',
    component: () => import('@/views/PersonalInfo.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/driver/auth',
    name: 'DriverAuth',
    component: () => import('@/views/DriverAuth.vue'),
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 导航守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router
