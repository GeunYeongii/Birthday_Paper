<!--
  name : 이에닮
  desc : intro
  date : 2022-01-05
-->
<template>
  <v-container>
    <div class="intro">
      <v-card elevation="3" class="intro-logo">
        <v-card-text>
          <v-img src="@/assets/img/logo.png"></v-img>
        </v-card-text>
      </v-card>

      <v-card elevation="0" class="mt-4">
        <v-card-actions bottom>
          <div class="mauto">
            <v-btn color="primary" @click="goLogin()" rounded dark elevation="3">
              로그인
            </v-btn>
            <v-btn class="ml-4" color="primary" @click="goJoin()" rounded dark elevation="3">
              회원가입
            </v-btn>
          </div>
        </v-card-actions>
      </v-card>

    </div>
  </v-container>
</template>

<script>

export default {
  name: 'Intro',
  components: {
  },
  filters: {
  },
  data () {
    return {
    }
  },
  created () {
  },
  mounted () {
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
