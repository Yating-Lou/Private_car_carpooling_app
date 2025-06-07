<template>
  <div class="trip-form-container">
    <div class="overlay">
      <div class="form-wrapper max-w-xl mx-auto p-8 rounded-lg shadow-lg bg-black bg-opacity-70 text-white">
        <h1 class="text-3xl font-extrabold mb-6 text-center">分享共享行程</h1>

        <form @submit.prevent="submitTrip" class="space-y-6">
          <div>
            <label class="block font-semibold mb-2" for="time">行程时间</label>
            <input
                id="time"
                v-model="form.time"
                type="datetime-local"
                class="input-field"
                required
            />
          </div>

          <div>
            <label class="block font-semibold mb-2" for="person">可共享人数</label>
            <input
                id="person"
                v-model.number="form.person"
                type="number"
                min="1"
                class="input-field"
                required
            />
          </div>

          <div>
            <label class="block font-semibold mb-2" for="carnumber">共享车牌号</label>
            <select
                id="carnumber"
                v-model="form.carnumber"
                class="input-field"
                required
            >
              <option disabled value="">请选择车辆</option>
              <option v-for="car in myCars" :key="car" :value="car">{{ car }}</option>
            </select>
          </div>

          <div>
            <label class="block font-semibold mb-2" for="pickup">起始位置</label>
            <input
                id="pickup"
                v-model="form.pickup"
                type="text"
                class="input-field"
                required
            />
          </div>

          <div>
            <label class="block font-semibold mb-2" for="dropoff">终止位置</label>
            <input
                id="dropoff"
                v-model="form.dropoff"
                type="text"
                class="input-field"
                required
            />
          </div>

          <div>
            <label class="block font-semibold mb-2" for="money">预估车费 (元)</label>
            <input
                id="money"
                v-model.number="form.money"
                type="number"
                min="0"
                class="input-field"
                required
            />
          </div>

          <button
              type="submit"
              class="submit-btn"
              :disabled="!isFormValid"
          >
            确认并发布
          </button>
        </form>

        <div
            v-if="submitted"
            class="mt-6 p-4 rounded bg-green-600 text-white text-center font-semibold"
        >
          行程发布成功！跳转到详情页面
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TripForm',
  data () {
    return {
      isDriver: true,
      myCars: ['京A12345', '沪B67890', '粤C13579'],
      form: {
        time: '',
        person: null,
        carnumber: '',
        pickup: '',
        dropoff: '',
        money: null
      },
      submitted: false
    }
  },
  computed: {
    isFormValid () {
      // 判断所有必填字段是否有效且非空
      return (
        this.form.time &&
        this.form.person >= 1 &&
        this.form.carnumber &&
        this.form.pickup.trim() !== '' &&
        this.form.dropoff.trim() !== '' &&
        this.form.money !== null &&
        this.form.money >= 0
      )
    }
  },
  methods: {
    submitTrip () {
      if (!this.isFormValid) return

      this.submitted = true

      // 跳转到 /tripdetail 页面
      this.$router.push('/tripdetail')

      // 重置表单
      this.resetForm()

      // 3秒后关闭提示
      setTimeout(() => {
        this.submitted = false
      }, 3000)
    },
    resetForm () {
      this.form = {
        time: '',
        person: null,
        carnumber: '',
        pickup: '',
        dropoff: '',
        money: null
      }
    }
  }
}
</script>

<style scoped>
.trip-form-container {
  min-height: 100vh;
  background-image: url('~@/assets/TripFormbackground.jpeg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.overlay {
  background: rgba(0, 0, 0, 0.65);
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.7);
}

.form-wrapper {
  color: #eee;
}

/* 统一输入框样式 */
.input-field {
  width: 100%;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  border: none;
  font-size: 1rem;
  outline: none;
  transition: box-shadow 0.3s ease;
  box-sizing: border-box;
}

.input-field:focus {
  box-shadow: 0 0 6px 2px #3b82f6;
  background-color: #222;
  color: white;
}

/* 禁用按钮样式 */
.submit-btn {
  margin-top: 1.5rem;
  width: 100%;
  background-color: #3b82f6;
  color: white;
  padding: 0.75rem;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1.1rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:disabled {
  background-color: #94a3b8;
  cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
  background-color: #2563eb;
}
</style>
