<template>
  <div class="home-container">
    <TopNav />
    <div class="main-content">
      <!-- 出行页面 -->
      <div v-if="activeTab === 'trip'">
        <el-card class="function-card">
          <el-button type="primary" @click="goToTripForm" style="width: 100%; margin-bottom: 20px;">
            分享共享行程
          </el-button>
          <el-button type="success" @click="goToTripList" style="width: 100%; margin-bottom: 20px;">
            查看共享行程
          </el-button>
          <el-button type="info" @click="goToOrderList" style="width: 100%">
            订单
          </el-button>
        </el-card>
      </div>

      <!-- 个人页面 -->
      <div v-if="activeTab === 'personal'">
        <el-card class="personal-card">
          <div class="user-info">
            <el-avatar :size="80" :src="userAvatar" />
            <div class="info-text">
              <h3>{{ userInfo.name }}</h3>
              <p>{{ userInfo.phone }}</p>
              <p>{{ userInfo.email || '暂无邮箱' }}</p>
            </div>
          </div>
          <div class="function-buttons">
            <el-button type="primary" @click="goToPersonalInfo" style="width: 100%; margin-bottom: 15px;">
              个人信息修改
            </el-button>
            <el-button type="warning" @click="goToDriverAuth" style="width: 100%">
              司机认证
            </el-button>
          </div>
        </el-card>
      </div>
    </div>

    <div class="bottom-tab">
      <el-menu
        :default-active="activeTab"
        mode="horizontal"
        @select="handleTabChange"
        class="tab-menu"
      >
        <el-menu-item index="trip">
          <span>出行</span>
        </el-menu-item>
        <el-menu-item index="personal">
          <span>个人</span>
        </el-menu-item>
      </el-menu>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import TopNav from '@/components/TopNav.vue'
import { checkDriverAuth } from '@/api/index.js'

export default {
  components: {
    TopNav
  },
  setup () {
    const router = useRouter()
    const activeTab = ref('trip')
    const userInfo = ref({})
    const isDriver = ref(false)
    const userAvatar = ref('https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png')

    onMounted(() => {
      const user = JSON.parse(localStorage.getItem('userInfo'))
      if (user) {
        userInfo.value = user
        checkDriverStatus(user.id)
      }
    })

    const checkDriverStatus = async (userId) => {
      try {
        const res = await checkDriverAuth(userId)
        isDriver.value = res.data.isDriver
      } catch (error) {
        console.error('检查司机认证状态失败:', error)
      }
    }

    const handleTabChange = (key) => {
      activeTab.value = key
    }

    const goToTripForm = () => {
      if (isDriver.value) {
        router.push('/trip/form')
      } else {
        ElMessage.warning('您尚未进行司机认证，无法714发布行程')
      }
    }

    const goToTripList = () => {
      router.push('/trip/list')
    }

    const goToOrderList = () => {
      router.push('/order/list')
    }

    const goToPersonalInfo = () => {
      router.push('/personal/info')
    }

    const goToDriverAuth = () => {
      router.push('/driver/auth')
    }

    return {
      activeTab,
      userInfo,
      userAvatar,
      handleTabChange,
      goToTripForm,
      goToTripList,
      goToOrderList,
      goToPersonalInfo,
      goToDriverAuth
    }
  }
}
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.main-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
.function-card, .personal-card {
  margin-bottom: 20px;
}
.user-info {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.info-text {
  margin-left: 20px;
}
.info-text h3 {
  margin: 0 0 5px 0;
}
.info-text p {
  margin: 5px 0;
  color: #666;
}
.bottom-tab {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}
.tab-menu {
  display: flex;
  justify-content: space-around;
}
.tab-menu .el-menu-item {
  flex: 1;
  text-align: center;
}
</style>
