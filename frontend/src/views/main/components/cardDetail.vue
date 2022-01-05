<!--
  name : 이에닮
  desc : cardDetail
  date : 2022-01-05
-->
<template>
  <v-dialog
    v-model="cardDetailDialog"
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
          <v-btn class="mauto" color="primary" @click="close()" rounded dark elevation="3">
            확인
          </v-btn>
        </v-card-actions>

    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: 'CardDetail',
  components: {
  },
  filters: {
  },
  data () {
    return {
      cardDetailDialog: false
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    open() {
      this.cardDetailDialog = true
    },
    close() {
      this.cardDetailDialog = false
    }
  }
}
</script>
