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
                  :rules="textRules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters>
                <v-text-field
                  v-model="joinData.pw"
                  label="PW"
                  :type="'password'"
                  :rules="textRules"
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
                  :rules="textRules"
                  hide-details
                ></v-text-field>
              </v-row>
              <v-row no-gutters class="mt-2">
                <date-picker
                  v-model="joinData.birth"
                  label="생년월일"
                  :rules="textRules"
                  range/>
              </v-row>
              <v-row no-gutters>
                <v-file-input
                  v-model="joinData.profileImg"
                  label="프로필 이미지"
                  hide-details
                ></v-file-input>
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
import datePicker  from '@/components/datePicker'

export default {
  name: 'Join',
  components: {
    datePicker
  },
  data () {
    return {
      /* Rules */
      textRules: [
				v => !!v || '필수 입력값입니다. 입력해주세요.',
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
