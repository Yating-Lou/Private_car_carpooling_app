<template>
  <div class="bottom-tabbar">
    <div
      class="tab-item"
      :class="{ active: activeTab === 'travel' }"
      @click="handleSwitchTab('travel')"
    >
      <i class="el-icon-location-outline"></i>
      <span>出行</span>
    </div>
    <div
      class="tab-item"
      :class="{ active: activeTab === 'personal' }"
      @click="handleSwitchTab('personal')"
    >
      <i class="el-icon-user"></i>
      <span>个人中心</span>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, toRefs } from 'vue'

const props = defineProps({
  activeTab: String
})

const emit = defineEmits(['update:activeTab'])

const { activeTab } = toRefs(props)

function handleSwitchTab (tab) {
  emit('update:activeTab', tab)
}
</script>

<style scoped>
.bottom-tabbar {
  height: 50px;
  display: flex;
  background-color: #fff;
  border-top: 1px solid #eee;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 999;
}

.tab-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #666;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
}

.tab-item i {
  font-size: 20px;
  margin-bottom: 2px;
}

.tab-item.active {
  color: #409EFF;
}
</style>
