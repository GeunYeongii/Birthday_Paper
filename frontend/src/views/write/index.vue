<!--
  name : 이에닮
  desc : write
  date : 2022-01-05
-->

<template>
  <v-container>
    <s-header></s-header>
    <div class="main">

      <h2 class="text-gray">000님 에게 편지를 작성해 주세요!</h2>

      <v-divider></v-divider>

      <v-row justify="center" style="margin-bottom:30px">
        <v-col cols="12">

          <v-card class="mb-4">
            <v-card-text @click="openDetail()">
              <span>000님 에게 편지가 도착했어요!</span>
              <span class="f_rit">
                <v-icon color="info">{{ icons.mdiCheck }}</v-icon>
              </span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅅㅅㅅ님 에게 편지가 도착했어요!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅁㅁㅁㅁ님 에게 편지가 도착했어요!</span>
              <span class="f_rit">
                <v-icon color="info">{{ icons.mdiCheck }}</v-icon>
              </span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!</span>
              <span class="f_rit">
                <v-icon color="info">{{ icons.mdiCheck }}</v-icon>
              </span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4">
            <v-card-text>
              <span>ㅇㅇ님 에게 편지가 도착했어요!!</span>
            </v-card-text>
          </v-card>

          <v-card class="mb-4 text-center" elevation="0">
            <v-card-text>
              <h5>아직 받은 편지가 없습니다</h5>
              <h5>편지를 작성해서 000님의 생일을 축하해 주세요!</h5>
            </v-card-text>
          </v-card>

        </v-col>
      </v-row>
      <write-detail ref="writeDetail"></write-detail>

      <v-footer class="justify-center pl-0" style="background-color:#fff; padding:0px;" inset app>
        <v-btn class="mt-3 mb-3" color="primary" dark @click="write()">
          작성하기
        </v-btn>
      </v-footer> 

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'
import writeDetail from '@/views/write/components/writeDetail'
import { mdiCheck } from '@mdi/js'

export default {
  name: 'Write',
  components: {
    SHeader,
    writeDetail
  },
  filters: {
  },
  data () {
    return {
      icons: {
        mdiCheck
      },
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    write() {
      this.$refs.writeDetail.open()
    }
  }
}
</script>
