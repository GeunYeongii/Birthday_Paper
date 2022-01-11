<!--
  name : 이에닮
  desc : join
  date : 2022-01-11
-->
<template>
  <div class="join">
    <v-row no-gutters justify="center" class="mt-8">

      <v-col no-gutters cols="12" class="text-center">
        <v-img
          class="m-auto mt-4 mb-2"
          max-width="125px"
          width="23vw"
          src="@/assets/img/cake.png"
          @click="goIntro()"></v-img>
        <p class="h6 txtC_474775">BIRTHDAY PAPER</p>
      </v-col>
    </v-row>
      
      <v-col no-gutters cols="12" class="pl-12 pr-12">
        <v-card width="90vw" class="m-auto shadow_eft">
          <v-card-text>
            <form ref="joinForm">
              <v-row no-gutters>
                <v-text-field
                  label="ID"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  label="PW"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  label="PW 체크"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  label="닉네임"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  label="생년월일"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  label="프로필 이미지"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters class="mt-4">
                <v-btn text class="txtC_474775" @click="joinStart()">
                  회원가입
                </v-btn>
              </v-row>
            </form>
          </v-card-text>
        </v-card>
      </v-col>

  </div>
</template>

<script>

export default {
  name: 'Join',
  data () {
    return {
      rules: [
        value => !!value || 'Required.',
      ],
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    goIntro(){
      this.$router.push('/')
    },
    joinStart(){
      
    }
  }
}
</script>
