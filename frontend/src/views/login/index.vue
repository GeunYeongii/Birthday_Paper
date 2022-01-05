<!--
  name : 이에닮
  desc : login
  date : 2022-01-05
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="login">

      <h1>로그인</h1>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">
          <v-card>
            <v-card-text>

              <form ref="joinForm">
                <v-row no-gutters>
                  <v-text-field
                    label="ID"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="PW"
                    :rules="rules"
                  ></v-text-field>
                </v-row>
              </form>

            </v-card-text>

            <v-card-actions>
              <div class="mauto">
                <v-btn color="primary" @click="login()" rounded dark>
                  로그인
                </v-btn>
                <v-btn class="ml-4" color="primary" @click="goJoin()" rounded dark>
                  회원가입
                </v-btn>
              </div>
            </v-card-actions>
          </v-card>
          
        </v-col>
      </v-row>

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'Login',
  components: {
    SHeader
  },
  filters: {
  },
  data () {
    return {
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    login(){
      this.$router.push('/main')
    },
    goJoin(){
      this.$router.push('/join')
    }
  }
}
</script>
