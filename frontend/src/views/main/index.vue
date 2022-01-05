<!--
  name : 이에닮
  desc : main
  date : 2022-01-05
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="main">

      <h2>n개의 편지가 걸렸어요!</h2>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">
          <v-card class="main_card">
            <div class="scroll_bar">  
              <v-card-text>

              </v-card-text>
            </div>
          </v-card>
          
          <v-card-actions>
            <v-btn class="mauto" color="primary" @click="login()" rounded dark>
              공유하기
            </v-btn>
          </v-card-actions>
          
        </v-col>
      </v-row>

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'Main',
  components: {
    SHeader
  },
  filters: {
  },
  data () {
    return {
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style>
/* .scroll_bar {
  max-height: calc(100vh - 230px);
} */
</style>
