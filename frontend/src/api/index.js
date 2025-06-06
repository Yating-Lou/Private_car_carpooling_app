import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 10000
})

// 请求拦截器
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, error => {
  return Promise.reject(error)
})

// 响应拦截器
api.interceptors.response.use(response => {
  return response.data
}, error => {
  // 检查 error.response 是否存在
  if (error.response && error.response.status === 401) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('username')
    window.location.href = '/login'
  }
  // 添加通用错误处理
  const errorMsg = error.response?.data?.error || error.message || '网络错误，请检查后端服务'
  console.error('请求错误:', errorMsg, error)
  return Promise.reject(error)
})
export default api
