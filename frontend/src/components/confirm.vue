<!--
  name : 이예닮
  desc : Alert 다이얼로그
  date : 2022-01-15
-->
<template>
  <v-dialog
    v-model="visible"
    persistent
    :max-width="options.maxWidth"
    @click:outside="closeOutside">
    <v-card id="popStyle">
      <!--팝업 제목-->
      <v-card-title class="title">
        {{ title }}
      </v-card-title>
      <!--/팝업 제목-->
      <!--팝업 내용-->
      <v-card-text>
        <v-row no-gutters v-html="message"></v-row>
        <v-row no-gutters></v-row>
      </v-card-text>
      <!--/팝업 내용-->
      <!--<v-card-text v-html="message"></v-card-text>-->
      <!--팝업 버튼-->
      <v-card-actions class="justify-center">
        <v-btn text @click="confirm">확인</v-btn>
        <v-btn v-show="mode.toUpperCase() !== 'ALERT'" text @click="cancel">취소</v-btn>
      </v-card-actions>
      <!--/팝업 버튼-->
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: 'sec-confirm',
  data () {
    return {
      mode: '',
      visible: false,
      title: '',
      message: '',
      options: {
        maxWidth: 400
      },
      resolve: null,
      reject: null
    }
  },
  /* 
    <사용법>
    1. <s-confirm ref="confirm"></s-confirm> 추가한다.
    2. 함수에서 필요한 시점에 아래 설명대로 사용한다.
    this.$refs.confirm.open(signal, title, content).then(() => {
      action
    })
    - signal : 'alert' or 'confirm'
    - title : 알림창 또는 확인창의 타이틀
    - content : 알림창 또는 확인창의 내용
    - action : 알림창 또는 확인창의 확인 후 다음 행동. 다음 행동이 없으면 비워둬도됨.
    
    ex>
    this.$refs.confirm.open('confirm', '날짜 선택', '종료일이 시작일보다 먼저일 수 없습니다. 다시 선택해주세요.').then(() => {
      this.$router.push('gogo')
    })
    
    * signal이 'alert'인 경우 .then() 부터 생략가능
  */
  methods: {
    open (mode, title, message, options) {
      this.visible = true
      this.title = title
      this.message = message
      this.mode = mode
      this.options = Object.assign(this.options, options)
      return new Promise((resolve, reject) => {
        this.resolve = resolve
        this.reject = reject
      })
    },
    closeOutside () {
    },
    confirm () {
      this.resolve(true)
      this.visible = false
    },
    cancel () {
      this.visible = false
    }
  }
}
</script>
<style scoped>

</style>
