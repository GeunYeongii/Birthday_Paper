<!--
  name : 이에닮
  desc : write
  date : 2022-01-05
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="write">

      <h2>000님 에게 편지를 작성해 주세요!</h2>

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
            <v-btn
              class="mauto"
              color="primary"
              @click="write()"
              rounded
              dark
            >
              작성하기
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
  name: 'Write',
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
    write() {

    }
  }
}
</script>
