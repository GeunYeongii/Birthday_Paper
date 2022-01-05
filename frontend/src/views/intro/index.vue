<!--
  name : 이에닮
  desc : intro
  date : 2022-01-05
-->
<template>
  <v-container>
    <div class="intro">
      <v-card>
        <v-card-text>
          <v-img src="@/assets/img/logo.png"></v-img>
        </v-card-text>

        <v-card-actions bottom>
          <div class="mauto">
            <v-btn
              color="primary"
              @click="goLogin()"
              rounded
              dark
            >
              로그인
            </v-btn>
            <v-btn
              class="ml-4"
              color="primary"
              @click="goJoin()"
              rounded
              dark
            >
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
