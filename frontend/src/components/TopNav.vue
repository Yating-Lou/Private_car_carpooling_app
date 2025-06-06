<template>
  <div></div>
</template>

<script>
import axios from 'axios'
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'TopNav',
  setup () {
    const store = useStore()
    const username = computed(() => store.state.user?.name || '未登录')
    return {
      username
    }
  },
  mounted () {
    this.fetchUsername()
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    },
    goHome () {
      this.$router.push('/home')
    },
    async fetchUsername () {
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
