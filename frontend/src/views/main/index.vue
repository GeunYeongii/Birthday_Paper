<!--
  name : 이에닮
  desc : main
  date : 2022-01-05
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="main">

      <h2 class="text-gray">n개의 편지가 걸렸어요!</h2>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">
          <v-card class="main_card" elevation="3">
            <div class="scroll_bar">  
              <v-card-text>

              </v-card-text>
            </div>
          </v-card>
          
          <v-card-actions>
            <v-btn class="mauto" color="primary" @click="share()" rounded dark elevation="3">
              공유하기
            </v-btn>
          </v-card-actions>
          
        </v-col>
      </v-row>

    </div>
    <card-detail ref="cardDetail"></card-detail>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'
import cardDetail from '@/views/main/components/cardDetail'

export default {
  name: 'Main',
  components: {
    SHeader,
    cardDetail
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
    share() {
      
    }
  }
}
</script>
