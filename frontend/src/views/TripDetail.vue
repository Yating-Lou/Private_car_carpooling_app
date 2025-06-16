<template>
  <div class="trip-detail-container">
    <!-- 顶部导航栏 -->
    <TopNav />
    
    <!-- 行程详情内容 -->
    <div class="trip-content" v-if="tripData">
      <el-card class="trip-card" shadow="always">
        <!-- 订单号和状态 -->
        <div class="trip-header">
          <h3 class="trip-title">行程详情</h3>
          <el-tag 
            :type="getStatusType(tripData.status)" 
            size="medium"
            class="status-tag"
          >
            {{ tripData.status }}
          </el-tag>
        </div>
        
        <!-- 基本信息 -->
        <div class="trip-info-section">
          <div class="info-row">
            <i class="el-icon-document"></i>
            <span class="label">订单号：</span>
            <span class="value">{{ tripData.orderId }}</span>
          </div>
          
          <div class="info-row">
            <i class="el-icon-user-solid"></i>
            <span class="label">私家车主：</span>
            <span class="value">{{ tripData.driverName }}</span>
          </div>
          
          <div class="info-row">
            <i class="el-icon-phone"></i>
            <span class="label">联系电话：</span>
            <span class="value">
              <a :href="'tel:' + tripData.driverPhone" class="phone-link">
                {{ tripData.driverPhone }}
              </a>
            </span>
          </div>
          
          <div class="info-row">
            <i class="el-icon-time"></i>
            <span class="label">行程时间：</span>
            <span class="value">{{ formatTime(tripData.tripTime) }}</span>
          </div>
          
          <div class="info-row">
            <i class="el-icon-user"></i>
            <span class="label">可共享人数：</span>
            <span class="value">{{ tripData.currentPassengers }}/{{ tripData.maxPassengers }}</span>
          </div>
          
          <div class="info-row">
            <i class="el-icon-truck"></i>
            <span class="label">车牌号：</span>
            <span class="value">{{ tripData.carNumber }}</span>
          </div>
        </div>
        
        <!-- 路线信息 -->
        <div class="route-section">
          <h4 class="section-title">
            <i class="el-icon-location"></i>
            行程路线
          </h4>
          <div class="route-info">
            <div class="route-item start">
              <div class="route-dot start-dot"></div>
              <div class="route-text">
                <div class="location-label">起点</div>
                <div class="location-name">{{ tripData.startLocation }}</div>
              </div>
            </div>
            
            <div class="route-line"></div>
            
            <div class="route-item end">
              <div class="route-dot end-dot"></div>
              <div class="route-text">
                <div class="location-label">终点</div>
                <div class="location-name">{{ tripData.endLocation }}</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 费用信息 -->
        <div class="fare-section">
          <h4 class="section-title">
            <i class="el-icon-money"></i>
            费用信息
          </h4>
          <div class="fare-info">
            <span class="fare-label">预估车费：</span>
            <span class="fare-amount">¥{{ tripData.estimatedFare }}</span>
          </div>
        </div>
        
        <!-- 乘客列表（司机视角） -->
        <div v-if="userRole === 'driver' && tripData.passengers && tripData.passengers.length > 0" class="passengers-section">
          <h4 class="section-title">
            <i class="el-icon-user"></i>
            乘客信息
          </h4>
          <div class="passengers-list">
            <div v-for="passenger in tripData.passengers" :key="passenger.id" class="passenger-item">
              <div class="passenger-info">
                <span class="passenger-name">{{ passenger.name }}</span>
                <span class="passenger-phone">{{ passenger.phone }}</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 操作按钮 -->
        <div class="action-section">
          <!-- 乘客操作 -->
          <div v-if="userRole === 'passenger'">
            <el-button 
              v-if="tripData.status === '已拼车'"
              type="success" 
              size="large"
              @click="startTrip"
              :loading="updating"
              class="action-btn"
            >
              开始行程
            </el-button>
            
            <el-button 
              v-if="tripData.status === '行程进行中'"
              type="primary" 
              size="large"
              @click="completeTrip"
              :loading="updating"
              class="action-btn"
            >
              行程完成
            </el-button>
            
            <el-button 
              v-if="tripData.status === '未拼车'"
              type="danger" 
              size="large"
              @click="cancelTrip"
              :loading="updating"
              class="action-btn"
            >
              取消拼车
            </el-button>
          </div>
          
          <!-- 司机操作 -->
          <div v-if="userRole === 'driver'">
            <el-button 
              v-if="tripData.status === '已拼车'"
              type="success" 
              size="large"
              @click="startTrip"
              :loading="updating"
              class="action-btn"
            >
              开始行程
            </el-button>
            
            <el-button 
              v-if="tripData.status === '行程进行中'"
              type="primary" 
              size="large"
              @click="completeTrip"
              :loading="updating"
              class="action-btn"
            >
              行程完成
            </el-button>
            
            <el-button 
              v-if="tripData.status === '未拼车'"
              type="warning" 
              size="large"
              @click="cancelTrip"
              :loading="updating"
              class="action-btn"
            >
              取消发布
            </el-button>
          </div>
        </div>
      </el-card>
    </div>
    
    <!-- 加载状态 -->
    <div v-if="loading" class="loading-container">
      <el-loading :loading="true" text="加载中..." />
    </div>
    
    <!-- 空状态 -->
    <div v-if="!loading && !tripData" class="empty-container">
      <el-empty description="行程信息不存在或已被删除" />
      <el-button @click="goBack" class="back-btn">返回</el-button>
    </div>
  </div>
</template>

<script>
import TopNav from '@/components/TopNav.vue'
import axios from 'axios'

export default {
  name: 'TripDetail',
  components: {
    TopNav
  },
  data() {
    return {
      loading: false,
      updating: false,
      tripData: null,
      userRole: 'passenger' // 'driver' 或 'passenger'
    }
  },
  mounted() {
    this.loadTripDetail()
  },
  methods: {
    async loadTripDetail() {
      this.loading = true
      try {
        const orderId = this.$route.params.orderId
        const response = await axios.get(`/api/trips/${orderId}`)
        this.tripData = response.data.trip
        this.userRole = response.data.userRole || 'passenger'
      } catch (error) {
        console.error('加载行程详情失败:', error)
        this.$message.error('加载行程详情失败，请重试')
      } finally {
        this.loading = false
      }
    },
    
    async startTrip() {
      this.$confirm('确认开始行程吗？', '确认操作', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'info'
      }).then(async () => {
        this.updating = true
        try {
          await axios.post(`/api/trips/${this.tripData.orderId}/start`)
          this.tripData.status = '行程进行中'
          this.$message.success('行程已开始')
        } catch (error) {
          console.error('开始行程失败:', error)
          this.$message.error('开始行程失败，请重试')
        } finally {
          this.updating = false
        }
      })
    },
    
    async completeTrip() {
      this.$confirm('确认完成行程吗？完成后将跳转到支付界面。', '确认操作', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'success'
      }).then(async () => {
        this.updating = true
        try {
          await axios.post(`/api/trips/${this.tripData.orderId}/complete`)
          this.tripData.status = '已完成'
          this.$message.success('行程已完成')
          
          // 跳转到支付界面
          setTimeout(() => {
            this.$router.push({
              name: 'Payment',
              params: { orderId: this.tripData.orderId }
            })
          }, 1000)
          
        } catch (error) {
          console.error('完成行程失败:', error)
          this.$message.error('完成行程失败，请重试')
        } finally {
          this.updating = false
        }
      })
    },
    
    async cancelTrip() {
      const confirmText = this.userRole === 'driver' ? '确认取消发布此行程吗？' : '确认取消拼车吗？'
      this.$confirm(confirmText, '确认操作', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        this.updating = true
        try {
          await axios.post(`/api/trips/${this.tripData.orderId}/cancel`)
          this.tripData.status = '拼车失败'
          this.$message.success('操作成功')
          
          // 返回上一页
          setTimeout(() => {
            this.goBack()
          }, 1000)
          
        } catch (error) {
          console.error('取消操作失败:', error)
          this.$message.error('操作失败，请重试')
        } finally {
          this.updating = false
        }
      })
    },
    
    getStatusType(status) {
      const statusMap = {
        '未拼车': 'info',
        '拼车失败': 'danger',
        '已拼车': 'warning',
        '行程进行中': 'success',
        '已完成': 'success'
      }
      return statusMap[status] || 'info'
    },
    
    formatTime(timeString) {
      const date = new Date(timeString)
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
    },
    
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
.trip-detail-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding-bottom: 60px;
}

.trip-content {
  padding: 15px;
}

.trip-card {
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.trip-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 2px solid #f0f0f0;
}

.trip-title {
  margin: 0;
  color: #333;
  font-size: 20px;
  font-weight: bold;
}

.status-tag {
  font-size: 14px;
  padding: 8px 16px;
  border-radius: 20px;
}

.trip-info-section {
  margin-bottom: 25px;
}

.info-row {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  padding: 10px 0;
  border-bottom: 1px solid #f5f5f5;
}

.info-row i {
  color: #409eff;
  margin-right: 12px;
  width: 20px;
  font-size: 16px;
}

.label {
  font-weight: 500;
  color: #666;
  min-width: 80px;
  margin-right: 10px;
}

.value {
  color: #333;
  font-weight: normal;
  flex: 1;
}

.phone-link {
  color: #409eff;
  text-decoration: none;
}

.phone-link:hover {
  text-decoration: underline;
}

.section-title {
  margin: 0 0 15px 0;
  color: #333;
  font-size: 16px;
  font-weight: bold;
  display: flex;
  align-items: center;
}

.section-title i {
  margin-right: 8px;
  color: #409eff;
}

.route-section, .fare-section, .passengers-section {
  margin-bottom: 25px;
  padding: 20px;
  background: #fafafa;
  border-radius: 12px;
}

.route-info {
  position: relative;
}

.route-item {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.route-item.end {
  margin-bottom: 0;
}

.route-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 15px;
  flex-shrink: 0;
}

.start-dot {
  background-color: #67c23a;
}

.end-dot {
  background-color: #f56c6c;
}

.route-line {
  width: 2px;
  height: 20px;
  background-color: #ddd;
  margin-left: 5px;
  margin-bottom: 10px;
}

.route-text {
  flex: 1;
}

.location-label {
  font-size: 12px;
  color: #999;
  margin-bottom: 5px;
}

.location-name {
  font-size: 14px;
  color: #333;
  font-weight: 500;
}

.fare-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fare-label {
  font-size: 16px;
  color: #666;
}

.fare-amount {
  font-size: 24px;
  color: #f56c6c;
  font-weight: bold;
}

.passengers-list {
  background: white;
  border-radius: 8px;
  padding: 15px;
}

.passenger-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
}

.passenger-item:last-child {
  border-bottom: none;
}

.passenger-info {
  display: flex;
  flex-direction: column;
}

.passenger-name {
  font-weight: 500;
  color: #333;
  margin-bottom: 5px;
}

.passenger-phone {
  font-size: 14px;
  color: #666;
}

.action-section {
  margin-top: 30px;
  text-align: center;
}

.action-btn {
  width: 100%;
  height: 50px;
  font-size: 16px;
  font-weight: bold;
  border-radius: 25px;
  margin-bottom: 10px;
}

.loading-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.empty-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 120px);
  text-align: center;
}

.back-btn {
  margin-top: 20px;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .trip-content {
    padding: 10px;
  }
  
  .trip-title {
    font-size: 18px;
  }
  
  .info-row {
    flex-direction: column;
    align-items: flex-start;
    padding: 8px 0;
  }
  
  .label {
    min-width: auto;
    margin-bottom: 5px;
    font-size: 14px;
  }
  
  .value {
    font-size: 14px;
  }
  
  .fare-amount {
    font-size: 20px;
  }
  
  .route-section, .fare-section, .passengers-section {
    padding: 15px;
  }
}
</style>
