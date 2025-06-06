<script setup>
/* global defineProps, defineEmits */

import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import BottomTabBar from '@/components/BottomTabBar.vue'

const router = useRouter()
const activeTab = ref('personal')

const props = defineProps({
  userInfo: {
    type: Object,
    default: () => ({ avatar: '', name: '匿名', phone: '暂无信息' })
  },
  isDriver: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['editPersonalInfo', 'driverAuth', 'logout'])

function handleLogout () {
  emit('logout')
  router.push('/login')
}

// 监听 activeTab 变化，切换路由
watch(activeTab, (newTab) => {
  if (newTab === 'travel' && router.currentRoute.value.path !== '/home') {
    router.push('/home')
  }
})
</script>

<template>
  <div class="personal-tab">
    <div class="user-info-card">
      <div class="avatar">
        <el-avatar :size="80" :src="props.userInfo.avatar || require('@/assets/default-avatar.png')" />
      </div>
      <div class="info">
        <div class="name">{{ props.userInfo.name }}</div>
        <div class="phone">{{ props.userInfo.phone }}</div>
        <div class="driver-status" :class="{ 'is-driver': props.isDriver }">
          {{ props.isDriver ? '已认证司机' : '未认证司机' }}
        </div>
      </div>
    </div>

    <div class="menu-list">
      <el-menu>
        <el-menu-item @click="emit('editPersonalInfo')">
          <i class="el-icon-user"></i>
          <span>个人信息</span>
        </el-menu-item>
        <el-menu-item @click="emit('driverAuth')">
          <i class="el-icon-s-check"></i>
          <span>司机认证</span>
        </el-menu-item>
        <el-menu-item @click="emit('histBill')">
          <i class="el-icon-s-check"></i>
          <span>历史订单</span>
        </el-menu-item>
        <el-menu-item @click="handleLogout">
          <i class="el-icon-switch-button"></i>
          <span>退出登录</span>
        </el-menu-item>
      </el-menu>
    </div>

    <!-- 底部导航栏 -->
    <BottomTabBar v-model:activeTab="activeTab" />
  </div>
</template>

<style scoped>
.personal-tab {
  padding: 15px;
}

.user-info-card {
  margin: 0 15px 15px 15px;
  background-color: #fff;
  border-radius: 10px;
  padding: 40px;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.avatar {
  margin-left: 20px;
  margin-right: 15px;
}

.info {
  flex: 1;
}

.name {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.phone {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.driver-status {
  font-size: 12px;
  color: #fff;
  background-color: #f56c6c;
  padding: 4px 8px;
  border-radius: 10px;
  display: inline-block;
}

.driver-status.is-driver {
  background-color: #67c23a;
}

.menu-list {
  margin-top: 50px;
  margin-left: 15px;
  margin-right: 15px;
  background-color: #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.menu-list .el-menu {
  border-right: none;
}

.menu-list .el-menu-item {
  font-size: 15px;
  height: 50px;
  line-height: 50px;
}

.menu-list .el-menu-item i {
  margin-right: 5px;
}
</style>
