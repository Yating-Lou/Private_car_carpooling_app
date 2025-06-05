<template>
  <div class="top-nav">
    <el-menu mode="horizontal">
      <el-menu-item index="back" @click="goBack">
        <el-icon><ArrowLeft /></el-icon>
        <span>返回</span>
      </el-menu-item>
      <el-menu-item index="home" @click="goHome">
        <el-icon><HomeFilled /></el-icon>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item index="user" style="float: right">
        <span>{{ userName }}</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, HomeFilled } from '@element-plus/icons-vue'

export default {
  components: {
    ArrowLeft,
    HomeFilled
  },
  setup() {
    const router = useRouter()
    const userName = ref('')

    const userInfo = JSON.parse(localStorage.getItem('userInfo'))
    if (userInfo) {
      userName.value = userInfo.name
    }

    const goBack = () => {
      router.go(-1)
    }

    const goHome = () => {
      router.push('/home')
    }

    return {
      userName,
      goBack,
      goHome
    }
  }
}
</script>

<style scoped>
.top-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
}
</style>