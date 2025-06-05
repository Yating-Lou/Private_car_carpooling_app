import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 5000
})

instance.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// 登录接口
export const login = (data) => {
  return instance.post('/auth/login', data)
}

// 注册接口
export const register = (data) => {
  return instance.post('/auth/register', data)
}

// 检查司机认证状态
export const checkDriverAuth = (userId) => {
  return instance.get(`/user/driver-status?userId=${userId}`)
}

export default instance
