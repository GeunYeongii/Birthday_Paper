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
          class="m-auto mt-8 mb-4 cursor_pointer"
          max-width="125px"
          width="23vw"
          src="@/assets/img/cake.png"
          @click="goIntro()"></v-img>
        <p class="h6 txtC_474775">BIRTHDAY PAPER</p>
      </v-col>
      
      <v-col no-gutters cols="12" class="pl-12 pr-12">
        <v-card width="90vw" class="m-auto shadow_eft">
          <v-card-text>
            <v-form ref="loginForm">
              <v-row no-gutters>
                <v-text-field
                  class="m-0 p-0"
                  v-model="email"
                  label="EMAIL"
                  :rules="emailRules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  class="m-0 mt-4 p-0"
                  v-model="password"
                  label="PW"
                  :type="'password'"
                  :rules="textRules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters class="mt-4">
                <v-btn text color="secondary" class="txtC_474775" @click="loginStart()">
                  로그인
                </v-btn>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>

      <p class="text-center mt-4 txtC_474775">
        Don't have an account? <span class="text-decoration-underline cursor_pointer" @click="goJoin()">Sign Up.</span>
      </p>

    </v-row>

    <s-confirm ref="confirm"></s-confirm>
    <s-spinner ref="spinner"></s-spinner>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      email: '',
      password: '',
      textRules: [
				v => !!v || '필수 입력값입니다. 입력해주세요.'
      ],
      emailRules: [
				v => !!v || '필수 입력값입니다. 입력해주세요.',
				v => /.+@.+\..+/.test(v) || '이메일 형식을 확인 해주세요.'
      ]
    }
  },
  methods: {
    loginStart(){
      if (this.$refs.loginForm.validate()) {
        this.$refs.spinner.open()
        this.$store.dispatch('Login', { email: this.email, pw: this.password }).then(response => {
          this.$refs.spinner.close()
          if (response.code == 20000) {
            this.$router.push('/main')
          } else {
            this.$refs.confirm.open('alert','로그인 실패',response.message)
          }
        }).catch(e => {
          this.$refs.spinner.close()
          console.log(e)
        })
      } else {
        this.$refs.confirm.open('alert','로그인 실패','아이디 / 패스워드를 입력해주세요.')
      }
    },
    goIntro(){
      this.$refs.spinner.open()
      this.$router.push('/').then(() => {
        this.$refs.spinner.close()
      })
    },
    goJoin(){
      this.$refs.spinner.open()
      this.$router.push('/join').then(() => {
        this.$refs.spinner.close()
      })
    }
  }
}
</script>

<style>
</style>
