<template>
  <div class="register-container">
    <top-nav title="注册账号" :show-home="false"></top-nav>

    <div class="form-container">
      <el-form :model="registerForm" :rules="registerRules" ref="registerFormRef">
        <el-form-item prop="name">
          <el-input
            v-model="registerForm.name"
            placeholder="请输入姓名"
            prefix-icon="el-icon-user"
          ></el-input>
        </el-form-item>

        <el-form-item prop="phone">
          <el-input
            v-model="registerForm.phone"
            placeholder="请输入手机号"
            prefix-icon="el-icon-mobile-phone"
          ></el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input
            v-model="registerForm.password"
            placeholder="请输入密码"
            prefix-icon="el-icon-lock"
            show-password
          ></el-input>
        </el-form-item>

        <el-form-item prop="confirmPassword">
          <el-input
            v-model="registerForm.confirmPassword"
            placeholder="请确认密码"
            prefix-icon="el-icon-lock"
            show-password
          ></el-input>
        </el-form-item>

        <el-form-item prop="email">
          <el-input
            v-model="registerForm.email"
            placeholder="请输入邮箱（可选）"
            prefix-icon="el-icon-message"
          ></el-input>
        </el-form-item>

        <el-form-item prop="smsCode">
          <div class="sms-code-input">
            <el-input
              v-model="registerForm.smsCode"
              placeholder="请输入验证码"
              prefix-icon="el-icon-key"
            ></el-input>
            <el-button
              type="primary"
              class="sms-btn"
              @click="sendSmsCode"
              :disabled="smsBtnDisabled"
            >{{ smsBtnText }}</el-button>
          </div>
        </el-form-item>

        <el-button
          type="primary"
          class="register-btn"
          @click="handleRegister"
          :loading="loading"
        >注册</el-button>
      </el-form>

      <div class="login-tip">
        已有账号？<span @click="goToLogin">立即登录</span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import TopNav from '@/components/TopNav.vue'

export default {
  name: 'RegisterPage',
  components: {
    TopNav
  },
  setup () {
    const router = useRouter()
    const registerFormRef = ref(null)
    const loading = ref(false)
    const smsBtnDisabled = ref(false)
    const smsBtnText = ref('获取验证码')

    const registerForm = reactive({
      name: '',
      phone: '',
      password: '',
      confirmPassword: '',
      email: '',
      smsCode: ''
    })

    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== registerForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }

    const registerRules = {
      name: [
        { required: true, message: '请输入姓名', trigger: 'blur' },
        { min: 2, max: 10, message: '长度在2到10个字符', trigger: 'blur' }
      ],
      phone: [
        { required: true, message: '请输入手机号', trigger: 'blur' },
        { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, max: 20, message: '长度在6到20个字符', trigger: 'blur' }
      ],
      confirmPassword: [
        { required: true, validator: validatePass, trigger: 'blur' }
      ],
      smsCode: [
        { required: true, message: '请输入验证码', trigger: 'blur' },
        { pattern: /^\d{6}$/, message: '验证码为6位数字', trigger: 'blur' }
      ]
    }

    const handleRegister = () => {
      registerFormRef.value.validate((valid) => {
        if (valid) {
          loading.value = true
          // 模拟注册成功，直接跳转到登录页面
          setTimeout(() => {
            ElMessage.success('注册成功')
            loading.value = false
            router.push('/login')
          }, 1000) // 模拟 1 秒延迟
        }
      })
    }

    const sendSmsCode = () => {
      if (!registerForm.phone) {
        ElMessage.error('请输入手机号')
        return
      }

      smsBtnDisabled.value = true
      let countdown = 60
      smsBtnText.value = `${countdown}秒后重试`

      const timer = setInterval(() => {
        countdown--
        smsBtnText.value = `${countdown}秒后重试`

        if (countdown <= 0) {
          clearInterval(timer)
          smsBtnDisabled.value = false
          smsBtnText.value = '获取验证码'
        }
      }, 1000)

      // 模拟发送验证码
      ElMessage.success('验证码已发送')
    }

    const goToLogin = () => {
      router.push('/login')
    }

    return {
      registerForm,
      registerRules,
      registerFormRef,
      loading,
      smsBtnDisabled,
      smsBtnText,
      handleRegister,
      sendSmsCode,
      goToLogin
    }
  }
}
</script>

<style scoped>
.register-container {
  height: 100vh;
  background-color: #f5f5f5;
}

.form-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
}

::v-deep(.el-input__inner) {
  height: 48px;
  border-radius: 24px;
  font-size: 16px;
}

::v-deep(.el-input) {
  width: 80%;
  margin-left: 45px;
  margin-top: 10px;
}

.el-form-item {
  margin-bottom: 24px;
}

.sms-code-input {
  display: flex;
  align-items: center;
}

.sms-btn {
  width: 100px;
  height: 44px;
  border-radius: 24px;
  flex-shrink: 0;
  margin-left: 20px;
  margin-top: 10px;
}

.register-btn {
  width: 60%;
  height: 48px;
  font-size: 16px;
  margin-top: 20px;
  border-radius: 24px;
}

.login-tip {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.login-tip span {
  color: #409EFF;
  cursor: pointer;
}
</style>
