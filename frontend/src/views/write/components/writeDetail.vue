<!--
  name : 이에닮
  desc : writeDetail
  date : 2022-01-05
-->
<template>
  <v-dialog
    v-model="writeDetailDialog"
    persistent
    scrollable>

    <v-card id="popupBox" class="popupBox_pcNheightA">
      <v-card-title class="pop_title_2">
      </v-card-title>
      
        <v-card-text class="conTR_reJ_txtinP">
          <v-container>
            <v-row no-gutters>
              <v-col cols="12">
                testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions class="pop_boT_btnCon justify-center">
          <v-btn class="mauto" color="primary" @click="sendMassage()" rounded dark elevation="3">
            저장하기
          </v-btn>
          <v-btn class="mauto" color="primary" @click="close()" rounded dark elevation="3">
            닫기
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
      writeDetailDialog: false
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    sendMassage() {

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
