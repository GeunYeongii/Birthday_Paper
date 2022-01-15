<!--
  name : 이예닮
  desc : Alert 다이얼로그
  date : 2022-01-15
-->
<template>
  <v-row justify="center">
    <v-dialog
      v-model="alertDialog"
      persistent
      max-width="290"
    >
      <v-card>
        <v-card-title class="text-h6">
          {{title}}
        </v-card-title>

        <v-card-text>
          {{text}}
        </v-card-text>

        <v-card-actions>
          <v-row no-gutters>
            <v-btn text @click="close()">
              확인
            </v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        alertDialog: false,
        title: '',
        text: ''
      }
    },
    methods: {
      open(title, text) {
        this.title = title
        this.text = text
        this.alertDialog = true
      },
      close() {
        this.alertDialog = false
      }
    }
  }
</script>