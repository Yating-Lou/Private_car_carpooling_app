<template>
  <div class="login-container">
    <el-card class="login-card">
      <h2>登录</h2>
      <el-form :model="loginForm" :rules="loginRules" ref="loginForm">
        <el-form-item prop="phone">
          <el-input v-model="loginForm.phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" placeholder="密码" show-password></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleLogin" style="width: 100%">登录</el-button>
        </el-form-item>
      </el-form>
      <div class="register-link">
        <span>还没有账号？</span>
        <el-button type="text" @click="goRegister">立即注册</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { login } from '@/api/index.js'

export default {
  setup () {
    const router = useRouter()
    const loginForm = ref({
      phone: '',
      password: ''
    })

    const loginRules = ref({
      phone: [
        { required: true, message: '请输入手机号', trigger: 'blur' },
        { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, max: 20, message: '长度在6到20个字符', trigger: 'blur' }
      ]
    })

    const handleLogin = async () => {
      try {
        const res = await login(loginForm.value)
        if (res.code === 200) {
          localStorage.setItem('token', res.data.token)
          localStorage.setItem('userInfo', JSON.stringify(res.data.user))
          ElMessage.success('登录成功')
          router.push('/home')
        } else {
          ElMessage.error(res.message)
        }
      } catch (error) {
        ElMessage.error('登录失败，请稍后重试')
      }
    }

    const goRegister = () => {
      router.push('/register')
    }

    return {
      loginForm,
      loginRules,
      handleLogin,
      goRegister
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.login-card {
  width: 400px;
  padding: 20px;
}
.register-link {
  text-align: center;
  margin-top: 10px;
}
</style>
