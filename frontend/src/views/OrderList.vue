<template>
  <div class="container">
    <div class="tabs">
      <button :class="{ active: currentTab === 'trips' }" @click="switchTab('trips')">查看共享行程</button>
      <button :class="{ active: currentTab === 'orders' }" @click="switchTab('orders')">我的订单</button>
    </div>

    <!-- 共享行程视图 -->
    <div v-if="currentTab === 'trips'">
      <div class="filter">
        <label>筛选状态：
          <select v-model="statusFilter">
            <option value="">全部</option>
            <option value="未拼车">未拼车</option>
            <option value="已拼车">已拼车</option>
            <option value="行程进行中">行程进行中</option>
            <option value="已完成">已完成</option>
          </select>
        </label>
      </div>
      <div v-for="trip in filteredTrips" :key="trip.id" class="card">
        <h3>时间：{{ trip.time }}</h3>
        <div>人数：{{ trip.seats }}</div>
        <div>起点：{{ trip.from }}</div>
        <div>终点：{{ trip.to }}</div>
        <div>状态：{{ trip.status }}</div>
        <button class="button" @click="showDetail(trip)">详情</button>
      </div>
    </div>

    <!-- 我的订单视图 -->
    <div v-if="currentTab === 'orders'">
      <div v-for="trip in trips" :key="trip.id" class="card">
        <div>订单号：{{ trip.id }}</div>
        <div>状态：{{ trip.status }}</div>
        <button class="button" @click="showDetail(trip)">详情</button>
      </div>
    </div>

    <!-- 行程详情视图 -->
    <div v-if="currentTab === 'detail'">
      <div class="card">
        <h3>订单号：{{ selectedTrip.id }}</h3>
        <div>车主：{{ selectedTrip.driver }}</div>
        <div>电话：{{ selectedTrip.phone }}</div>
        <div>时间：{{ selectedTrip.time }}</div>
        <div>人数：{{ selectedTrip.seats }}</div>
        <div>车牌：{{ selectedTrip.carNumber }}</div>
        <div>起点：{{ selectedTrip.from }}</div>
        <div>终点：{{ selectedTrip.to }}</div>
        <div>预估车费：{{ selectedTrip.fare }}</div>
        <div>状态：{{ selectedTrip.status }}</div>
        <button v-if="selectedTrip.status === '未拼车'" class="button" @click="alertAction('成功拼车')">拼车</button>
        <button v-if="selectedTrip.status === '行程进行中'" class="button" @click="alertAction('已完成，跳转支付')">已完成</button>
      </div>
      <button class="button back" @click="switchTab('trips')">返回</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const currentTab = ref('trips')
const statusFilter = ref('')
const selectedTrip = ref({})

const trips = ref([
  {
    id: '001',
    time: '2025-06-10 08:00',
    seats: 3,
    from: '中关村',
    to: '五道口',
    status: '未拼车',
    driver: '张三',
    phone: '13800000000',
    carNumber: '京A12345',
    fare: '¥30'
  },
  {
    id: '002',
    time: '2025-06-10 09:30',
    seats: 1,
    from: '清华园',
    to: '望京',
    status: '行程进行中',
    driver: '李四',
    phone: '13811111111',
    carNumber: '京B98765',
    fare: '¥45'
  }
])

const filteredTrips = computed(() => {
  return trips.value.filter(t => !statusFilter.value || t.status === statusFilter.value)
})

function switchTab (tab) {
  currentTab.value = tab
}

function showDetail (trip) {
  selectedTrip.value = trip
  currentTab.value = 'detail'
}

function alertAction (msg) {
  alert(msg)
}
</script>

<style scoped>
.container {
  font-family: sans-serif;
  padding: 20px;
  background: #f9f9f9;
}
.tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
.tabs button {
  padding: 10px 20px;
  cursor: pointer;
  border: none;
  background: #eee;
  border-radius: 5px;
}
.tabs button.active {
  background: #4caf50;
  color: white;
}
.card {
  background: white;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.card h3 {
  margin-top: 0;
}
.button {
  margin-top: 10px;
  padding: 6px 12px;
  border: none;
  background: #2196f3;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
.back {
  margin-top: 20px;
  background: #ccc;
}
.filter {
  margin-bottom: 15px;
}
</style>
