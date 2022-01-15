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
          class="m-auto mt-4 mb-2 cursor_pointer"
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
            <v-form ref="joinForm">
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.id"
                  label="ID"
                  color="secondary"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.pw"
                  label="PW"
                  :type="'password'"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="checkPw"
                  label="PW 체크"
                  :type="'password'"
                  :rules="pwCheckRules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.nickNm"
                  label="닉네임"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.birth"
                  label="생년월일"
                  :type="'date'"
                  :rules="rules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.profileImg"
                  label="프로필 이미지"
                  :type="'file'"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters class="mt-4">
                <v-btn text color="secondary" @click="joinStart()">
                  회원가입
                </v-btn>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>

  </div>
</template>

<script>
import { joinStart } from '@/api/join'

export default {
  name: 'Join',
  data () {
    return {
      rules: [
        value => !!value || 'Required.',
      ],
      pwCheckRules: [
        value => !!value || 'Required.',
        value => value == this.joinData.pw || 'Required.',
      ],
      joinData: {
        id:'',
        pw:'',
        nickNm:'',
        birth:'',
        profileImg:[]
      },
      checkPw:''
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    goIntro(){
      this.$router.push('/').catch(() => {})
    },
    joinStart(){
      if (this.$refs.joinForm.validate()) {
        joinStart(this.joinData).then(response => {
          if (response.code == 20000) {
            console.log('회원가입 성공')
            this.$router.push('/main').catch(() => {})
          } else {
            console.error('회원가입 실패')
          }
        })
      } else {
        console.error('빈 값을 넣어주세요')
      }
    }
  }
}
</script>
