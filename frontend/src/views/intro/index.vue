<!--
  name : 이에닮
  desc : intro
  date : 2022-01-11
-->
<template>
  <div class="intro">
    <v-row no-gutters justify="center" class="mt-8">

      <v-col no-gutters cols="12" class="text-center mb-6">
        <v-img
          class="m-auto mt-8 mb-4"
          max-width="125px"
          width="23vw"
          src="@/assets/img/cake.png"
          @click="goIntro()"></v-img>
        <p class="h6 txtC_474775">BIRTHDAY PAPER</p>
      </v-col>

      <v-col no-gutters cols="12" class="pl-6 pr-6">
        <v-row no-gutters>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft card_angle mt-3" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
          </v-col>
        </v-row>
      </v-col>
      
      <v-col no-gutters cols="12" class="mt-4 pl-6 pr-6">
        <v-row no-gutters>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
          </v-col>
          <v-col class="d-inline-block">
            <v-img class="m-auto shadow_eft card_angle" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
          </v-col>
        </v-row>
      </v-col>
      
      <v-btn text class="mt-8" @click="goLogin()">
        로그인
      </v-btn>
      <v-btn text @click="goJoin()">
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
