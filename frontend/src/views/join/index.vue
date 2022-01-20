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
                v-model="joinData.email"
                label="EMAIL"
                color="secondary"
                :rules="emailRules"
              ></v-text-field>
            </v-row>
            <v-row no-gutters>
              <v-text-field
                v-model="joinData.pw"
                label="PW"
                :type="'password'"
                :rules="textRules"
              ></v-text-field>
            </v-row>
            <v-row no-gutters>
              <v-text-field
                v-model="checkPw"
                label="PW 체크"
                :type="'password'"
                :rules="pwCheckRules"
              ></v-text-field>
            </v-row>
            <v-row no-gutters>
              <v-text-field
                v-model="joinData.nickNm"
                label="닉네임"
                :rules="textRules"
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
                name="file[]"
                label="프로필 이미지"
              ></v-file-input>
            </v-row>
            <v-row no-gutters>
              <v-btn text color="secondary" @click="joinStart()">
                회원가입
              </v-btn>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>

    <s-confirm ref="confirm"></s-confirm>
  </div>
</template>

<script>
import { joinStart } from '@/api/user'
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
      emailRules: [
				v => !!v || '필수 입력값입니다. 입력해주세요.',
				v => /.+@.+\..+/.test(v) || '이메일 형식을 확인 해주세요.'
      ],
      pwCheckRules: [
        v => !!v || '필수 입력값입니다. 입력해주세요.',
        v => v == this.joinData.pw || '비밀번호가 다릅니다.'
      ],
      joinData: {
        email:'',
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
      this.$router.push('/')
    },
    joinStart(){
      if (this.$refs.joinForm.validate()) {
        if (this.joinData.birth == []) {
          this.$refs.confirm.open('alert','회원가입 실패','생년월일을 입력해 주세요.')
          return
        }
        this.$refs.spinner.open()
        const data = new FormData()
        data.append('email', this.joinData.email)
        data.append('pw', this.joinData.pw)
        data.append('nickNm', this.joinData.nickNm)
        data.append('birth', this.joinData.birth)
        data.append('file[]', this.joinData.profileImg)

        joinStart(data).then(response => {
          this.$refs.spinner.close()
          if (response.code == 20000) {
            this.$refs.confirm.open('alert','회원가입 성공',response.message).then(() => {
              this.$router.push('/main')
            })
          } else {
            this.$refs.confirm.open('alert','회원가입 실패',response.message)
          }
        })
      } else {
        this.$refs.confirm.open('alert','회원가입 실패','필수값을 채워주세요.')
      }
    }
  }
}
</script>

<style>
.v-text-field__details {
  display: none;
}
</style>