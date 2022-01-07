<!--
  name : 이에닮
  desc : writeDetail
  date : 2022-01-05
-->
<template>
  <v-dialog v-model="writeDetailDialog">
    <v-card>
      <v-card-title class="pb-0">
        <v-row no-gutters>
          <v-text-field
            class="p-0"
            label="닉네임"
            v-model="nickName"
            :rules="rules"
          ></v-text-field>
        </v-row>
      </v-card-title>

      <v-card-text class="pb-0">
        <v-textarea
          class="p-0"
          label="편지의 내용을 작성해주세요"
          v-model="magData"
        ></v-textarea>
      </v-card-text>

      <v-card-actions class="pt-0">
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="sendMassage()">
          확인
        </v-btn>
      </v-card-actions>

    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: 'WriteDetail',
  components: {
  },
  filters: {
  },
  data () {
    return {
      writeDetailDialog: false,
      nickName: '',
      magData: '',
      rules: [
        value => !!value || '필수값 입니다',
      ],
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    sendMassage() {
      console.log(this.nickName)
      console.log(this.magData)
    },
    open() {
      this.writeDetailDialog = true
    },
    close() {
      this.writeDetailDialog = false
    }
  }
}
</script>
