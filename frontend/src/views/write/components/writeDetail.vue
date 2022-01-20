<!--
  name : 이에닮
  desc : cardDetail
  date : 2022-01-05
-->
<template>
  <div>
    <v-dialog max-width="550" v-model="writeDetailDialog" content-class="elevation-0">
      <v-img src="@/assets/img/asset_8.png">

        <div class="text-center writeDetail txtC_474775">
          <v-card-title class="pb-0">
            <v-row no-gutters>
              <v-text-field
                class="p-0"
                label="닉네임"
                v-model="sendParams.nickName"
                :rules="rules"
              ></v-text-field>
            </v-row>
          </v-card-title>
          
          <v-card-text class="pb-0 mt-4">
            <v-textarea
              class="p-0"
              label="편지의 내용을 작성해주세요"
              v-model="sendParams.magData"
            ></v-textarea>
          </v-card-text>
        </div>
        
        <v-col no-gutters cols="12" class="writeDetail-footer text-center">
          <v-btn text color="secondary" @click="close()">
            취소
          </v-btn>
          <v-btn text color="secondary" @click="sendMassage()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>

    <s-confirm ref="confirm"></s-confirm>

  </div>
</template>

<script>
import { sendMessage } from '@/api/letter'

export default {
  name: 'WriteDetail',
  components: {
  },
  filters: {
  },
  data () {
    return {
      writeDetailDialog: false,
      receiver: [],
      sendParams:{
        nickName: '',
        magData: ''
      },
      rules: [
        value => !!value || '필수값 입니다',
      ]
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    sendMassage() {
      sendMessage({receiver: this.receiver, sendParams: this.sendParams}).then(response => {
        if(response.code == 20000){
          this.$refs.confirm.open('alert','카드발송 완료', response.message).then(() => {
            location.reload()
          })
        } else {
          this.$refs.confirm.open('alert','카드발송 실패', response.message)
        }
      })
    },
    open(receiver) {
      this.receiver = receiver
      this.writeDetailDialog = true
    },
    close() {
      this.writeDetailDialog = false
    }
  }
}
</script>

<style>
.transparent {
   background-color: white!important;
   opacity: 0.65;
   border-color: transparent!important;
 }
</style>