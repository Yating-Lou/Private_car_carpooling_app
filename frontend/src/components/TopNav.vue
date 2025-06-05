<template>
  <div class="top-nav">
    <button @click="goBack">返回</button>
    <span class="username">欢迎，{{ username }}</span>
    <button @click="goHome">首页</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TopNav',
  data() {
    return {
      username: ''
    }
  },
  mounted() {
    this.fetchUsername()
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    },
    goHome() {
      this.$router.push('/home')  // 根据你的路由修改为主页面路径
    },
    async fetchUsername() {
      try {
        const token = localStorage.getItem('access_token')
        const response = await axios.get('/user/info', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        this.username = response.data.username
      } catch (error) {
        console.error('获取用户信息失败', error)
        this.username = '未登录'
      }
    }
  }
}
</script>

<style scoped>
.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #409EFF;
  padding: 10px 20px;
  color: white;
}

button {
  background: white;
  color: #409EFF;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  cursor: pointer;
}

.username {
  font-weight: bold;
}
</style>
