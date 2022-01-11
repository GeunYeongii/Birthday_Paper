<!--
  name : 이에닮
  desc : intro
  date : 2022-01-07
-->
<template>
  <div class="intro">
    <v-row no-gutters justify="center" class="mt-16 mb-2">
      <v-col cols="12">
        <v-img width="250" class="mauto mb-6"
          src="@/assets/img/cake.png"></v-img>

        <!-- <v-img width="210" class="mauto mb-6"
          src="@/assets/img/gift-box.png"></v-img> -->
      </v-col>
      
      <v-btn class="mb-2" color="primary" width="90vw" dark @click="goLogin()">
        로그인
      </v-btn>
      <v-btn class="mt-2" color="primary" width="90vw" dark @click="goJoin()">
        회원가입
      </v-btn>
    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Intro',
  data () {
    return {
    }
  },
  methods: {
    goLogin() {
      this.$router.push('/login')
    },
    goJoin() {
      this.$router.push('/join')
    }
  }
}
</script>
