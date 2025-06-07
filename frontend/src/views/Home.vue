<template>
  <div class="home-container">
    <TopNav />

    <div class="main-content">
      <div class="travel-tab">

        <!-- 顶部图片 -->
        <div class="banner-image-wrapper">
          <img src="@/assets/map.jpg" alt="共享出行" />
        </div>

        <!-- 出发地和目的地输入 -->
        <div class="location-inputs">
          <el-input
            v-model="startLocation"
            placeholder="请输入出发地点"
            clearable
            prefix-icon="el-icon-location"
          />
          <el-input
            v-model="endLocation"
            placeholder="请输入目的地"
            clearable
            prefix-icon="el-icon-location-outline"
          />
        </div>

        <!-- 按钮区域 -->
        <el-button
          type="primary"
          class="action-btn"
          @click="shareTrip"
          :disabled="!isDriver"
        >
          <i class="el-icon-share"></i>
          <span>发布共享行程</span>
          <span v-if="!isDriver" class="driver-tip">（司机）</span>
        </el-button>

        <el-button type="success" class="action-btn" @click="viewTrips">
          <i class="el-icon-search"></i>
          <span>查找共享行程</span>
          <span class="driver-tip">（乘客）</span>
        </el-button>

        <el-button type="info" class="action-btn" @click="viewOrders">
          <i class="el-icon-tickets"></i>
          <span>我的订单</span>
        </el-button>
      </div>
    </div>

    <BottomTabBar v-model:activeTab="activeTab" />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import TopNav from '@/components/TopNav.vue'
import BottomTabBar from '@/components/BottomTabBar.vue'

const router = useRouter()
const activeTab = ref('travel')
const isDriver = ref(false)
const startLocation = ref('')
const endLocation = ref('')

onMounted(() => {
  setTimeout(() => {
    isDriver.value = true
  }, 500)
})

watch(activeTab, (newTab) => {
  if (newTab === 'personal' && router.currentRoute.value.path !== '/person') {
    router.push('/person')
  } else if (newTab === 'travel' && router.currentRoute.value.path !== '/home') {
    router.push('/home')
  }
})

const shareTrip = () => {
  if (!isDriver.value) {
    ElMessage.error('请先完成司机认证')
    return
  }
  router.push('/tripform')
}

const viewTrips = () => {
  router.push('/trip/list')
}

const viewOrders = () => {
  router.push('/orderlist')
}
</script>

<script>
// 多词组件名，避免 ESLint 警告
export default {
  name: 'HomePage'
}
</script>

<style scoped>
.home-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  padding: 15px;
}

.travel-tab {
  display: flex;
  flex-direction: column;
  margin-top: 5px;
  gap: 20px;
  align-items: center;
}

.action-btn {
  width: 80%;
  height: 60px;
  display: flex;
  align-items: center;
  font-size: 18px;
  position: relative;
  border-radius: 25px;
  font-weight: bold;
}

.action-btn i {
  align-items: center;
  font-size: 18px;
}

.driver-tip {
  font-size: 12px;
  margin-left: 10px;
  color: white;
}

.banner-image-wrapper {
  width: 95%;
  text-align: center;
  margin-top: 10px;
  margin-bottom: 20px;
}

.banner-image-wrapper img {
  max-width: 100%;
  height: auto;
  border-radius: 20px;
  object-fit: contain;
}

.location-inputs {
  width: 80%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 20px;
}

.location-inputs .el-input {
  height: 48px;
  font-size: 20px;
}

</style>
