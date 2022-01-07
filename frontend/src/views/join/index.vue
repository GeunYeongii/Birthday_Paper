<!--
  name : 이에닮
  desc : join
  date : 2022-01-05
-->
<template>
  <div class="join">
      
    <v-row no-gutters justify="center" class="mt-12 mb-2">
      <v-col cols="12">
        <v-img width="250" class="mauto mb-4" @click="goIntro()"
          src="@/assets/img/logo_2.png"></v-img>

        <v-card elevation="3" width="90vw" class="mauto">
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

                <v-row no-gutters>
                  <v-text-field
                    label="PW 체크"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="닉네임"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="생년월일"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="프로필 이미지"
                  ></v-text-field>
                </v-row>
              </form>
          </v-card-text>
        </v-card>

      </v-col>

      <v-btn class="mauto mt-4" color="primary" width="90vw" dark @click="joinStart()">
        회원가입
      </v-btn>
    
    </v-row>



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
