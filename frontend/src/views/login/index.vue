<!--
  name : 이에닮
  desc : login
  date : 2022-01-07
-->
<template>
  <div class="login">
    <v-row no-gutters justify="center" class="mt-16 mb-2">
      <v-col cols="12" class="mt-6">
        <v-img width="250" class="mauto mb-6" @click="goIntro()"
          src="@/assets/img/logo.png"></v-img>

        <v-card elevation="3" width="90vw" class="mauto">
          <v-card-text>
            <form ref="joinForm">
              <v-row no-gutters>
                <v-text-field
                  v-model="form.id"
                  label="ID"
                  :rules="rules"
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="form.password"
                  label="PW"
                  :type="'password'"
                  :rules="rules"
                ></v-text-field>
              </v-row>
            </form>
          </v-card-text>
        </v-card>

      </v-col>

      <v-btn class="mauto mt-6" color="primary" width="90vw" dark @click="loginStart()">
        로그인
      </v-btn>

      <div class="mauto mt-12 text-gray accountText">
        Don't have an account? <a href="#" @click="goJoin()">Sign Up.</a>
      </div>
    
    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      form:{
        id: '',
        password: ''
      },
      rules: [
        value => !!value || '필수값 입니다',
      ],
    }
  },
  methods: {
    loginStart(){
      this.$router.push('/main')
    },
    goIntro(){
      this.$router.push('/')
    },
    goJoin(){
      this.$router.push('/join')
    }
  }
}
</script>

<style>
.accountText{
  text-align: center;
}
</style>
