<template>
  <div class="login-container">
    <div class="logo-area">
      <img src="@/assets/logo.png" alt="拼车App" class="app-logo">
      <h1>欢迎使用 同车共行</h1>
    </div>

    <div class="form-area">
      <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef">
        <el-form-item prop="phone">
          <el-input
            v-model="loginForm.phone"
            placeholder="请输入手机号"
            prefix-icon="el-icon-mobile-phone"
          ></el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            placeholder="请输入密码"
            prefix-icon="el-icon-lock"
            show-password
          ></el-input>
        </el-form-item>

        <el-button
          type="primary"
          class="login-btn"
          @click="handleLogin"
          :loading="loading"
        >登录</el-button>
      </el-form>

      <div class="other-options">
        <span @click="goToRegister">注册账号</span>
        <span @click="forgotPassword">忘记密码</span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

export default {
  name: 'LoginPage',
  setup () {
    const router = useRouter()
    const loginFormRef = ref(null)
    const loading = ref(false)

    const loginForm = ref({
      phone: '',
      password: ''
    })

    const loginRules = {
      phone: [
        { required: true, message: '请输入手机号', trigger: 'blur' },
        { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, max: 20, message: '长度在6到20个字符', trigger: 'blur' }
      ]
    }

    const handleLogin = () => {
      loginFormRef.value.validate((valid) => {
        if (valid) {
          loading.value = true
          // 模拟登录成功，直接跳转到首页
          setTimeout(() => {
            ElMessage.success('登录成功')
            loading.value = false
            router.push('/home')
          }, 1000) // 模拟 1 秒延迟
        }
      })
    }

    const goToRegister = () => {
      router.push('/register')
    }

    const forgotPassword = () => {
      ElMessage.info('请联系客服重置密码')
    }

    return {
      loginForm,
      loginRules,
      loginFormRef,
      loading,
      handleLogin,
      goToRegister,
      forgotPassword
    }
  }
}
</script>

<style scoped>
.login-container {
  padding: 20px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
}

.logo-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding-top: 160px;
  padding-bottom: 0px;
}

.app-logo {
  width: 100px;
  height: 100px;
  margin-bottom: 10px;
}

h1 {
  font-size: 24px;
  color: #333;
}

.form-area {
  height: 480px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 0;
}

.el-form {
  width: 60%;
  box-sizing: border-box;
}

.login-btn {
  width: 100%;
  height: 48px;
  font-size: 18px;
  margin-top: 20px;
  border-radius: 24px;
}

.other-options {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  color: #409EFF;
  font-size: 16px;
  width: 60%;
  max-width: 360px;
  padding: 0 10px;
  box-sizing: border-box;
}

.other-options span {
  cursor: pointer;
}

::v-deep(.el-input__inner) {
  height: 48px;
  font-size: 18px;
}
</style>
