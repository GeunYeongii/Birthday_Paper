<!--
  name : 이예닮
  desc : apinner 다이얼로그
  date : 2022-01-18
-->
<template>
  <div id="inspire">
    <v-layout row justify-center>
      <v-dialog v-model="apinnerDialog" persistent fullscreen content-class="loading-dialog">
        <v-container fill-height>
          <v-layout row justify-center align-center>
            <v-progress-circular indeterminate :size="70" :width="7" color="#474775"></v-progress-circular>
          </v-layout>
        </v-container>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        apinnerDialog: false,
        loading: true,
        sound: true,
        widgets: false
      }
    },
    methods: {
      open() {
        this.apinnerDialog = true
      },
      close() {
        this.apinnerDialog = false
      }
    }
  }
</script>

<style>
.loading-dialog{
  background-color: rgba(184, 184, 184, 0.5);
  height: 100%;
}
</style>