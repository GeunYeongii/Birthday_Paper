<!--
  name : 이에닮
  desc : login
  date : 2022-01-11
-->
<template>
  <div class="login">
    <v-row no-gutters justify="center" class="mt-8">

      <v-col no-gutters cols="12" class="text-center mb-5">
        <v-img
          class="m-auto mt-8 mb-4"
          max-width="125px"
          width="23vw"
          src="@/assets/img/cake.png"
          @click="goIntro()"></v-img>
        <p class="h6 txtC_474775">BIRTHDAY PAPER</p>
      </v-col>
      
      <v-col no-gutters cols="12" class="pl-12 pr-12">
        <v-card width="90vw" class="m-auto shadow_eft">
          <v-card-text>
            <form ref="joinForm">
              <v-row no-gutters>
                <v-text-field
                  class="m-0 p-0"
                  v-model="id"
                  label="ID"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  class="m-0 mt-4 p-0"
                  v-model="password"
                  label="PW"
                  :type="'password'"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters class="mt-4">
                <v-btn text class="txtC_474775" @click="goLogin()">
                  로그인
                </v-btn>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-col>

      <p class="text-center mt-4 txtC_474775">
        Don't have an account? <a href="#" class="txtC_474775" @click="goJoin()">Sign Up.</a>
      </p>

    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      id: '',
      password: '',
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

</style>
