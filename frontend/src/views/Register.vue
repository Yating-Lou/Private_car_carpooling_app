<template>
  <div class="register-container">
    <el-card class="register-card">
      <h2>注册</h2>
      <el-form :model="registerForm" :rules="registerRules" ref="registerForm">
        <el-form-item prop="name">
          <el-input v-model="registerForm.name" placeholder="姓名"></el-input>
        </el-form-item>
        <el-form-item prop="phone">
          <el-input v-model="registerForm.phone" placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="registerForm.password" placeholder="密码" show-password></el-input>
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input v-model="registerForm.confirmPassword" placeholder="确认密码" show-password></el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input v-model="registerForm.email" placeholder="邮箱（可选）"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleRegister" style="width: 100%">注册</el-button>
        </el-form-item>
      </el-form>
      <div class="login-link">
        <span>已有账号？</span>
        <el-button type="text" @click="goLogin">立即登录</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { register } from '@/api/index.js'

export default {
  setup () {
    const router = useRouter()
    const registerForm = ref({
      name: '',
      phone: '',
      password: '',
      confirmPassword: '',
      email: ''
    })

    const validatePass2 = (rule, value, callback) => {
      if (value !== registerForm.value.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }

    const registerRules = ref({
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
        { required: true, message: '请再次输入密码', trigger: 'blur' },
        { validator: validatePass2, trigger: 'blur' }
      ],
      email: [
        { type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur' }
      ]
    })

    const handleRegister = async () => {
      try {
        const res = await register(registerForm.value)
        if (res.code === 200) {
          ElMessage.success('注册成功')
          router.push('/login')
        } else {
          ElMessage.error(res.message)
        }
      } catch (error) {
        ElMessage.error('注册失败，请稍后重试')
      }
    }

    const goLogin = () => {
      router.push('/login')
    }

    return {
      registerForm,
      registerRules,
      handleRegister,
      goLogin
    }
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.register-card {
  width: 400px;
  padding: 20px;
}
.login-link {
  text-align: center;
  margin-top: 10px;
}
</style>
