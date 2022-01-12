<!--
  name : 이에닮
  desc : main
  date : 2022-01-12
-->
<template>
  <div class="main">
    <s-header></s-header>
    <v-col no-gutters cols="12" class="text-center">
      <v-img
        class="m-auto"
        max-width="125px"
        width="23vw"
        src="@/assets/img/cake.png"
        ></v-img>
    </v-col>
    <v-col no-gutters cols="12" class="text-center">
      <v-card height="50Vh" class="m-auto main_card" elevation="10">

        <div class="txtC_474775">
          <p class="pt-5">♥n개의 편지가 도착했어요♥</p>
        </div>

        <tiny-slider v-bind="tinySliderOptions" v-if="testList.length > 0">
          <div>
            <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
              <v-row no-gutters>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft card_angle mt-3" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
                </v-col>
              </v-row>
            </v-col>
            
            <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
              <v-row no-gutters>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft card_angle" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
                </v-col>
              </v-row>
            </v-col>
          </div>
          <div>
            <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
              <v-row no-gutters>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft card_angle mt-3" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
                </v-col>
              </v-row>
            </v-col>
            
            <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
              <v-row no-gutters>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_1.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_2.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_4.png"></v-img>
                </v-col>
                <v-col class="d-inline-block">
                  <v-img class="m-auto shadow_eft card_angle" max-width="90" width="16vw" src="@/assets/img/asset_3.png"></v-img>
                </v-col>
              </v-row>
            </v-col>
          </div>
        </tiny-slider>

        <div class="txtC_474775 no_latter" v-else>
          아직 받은 편지가 없습니다.<br>친구들에게 공유해서 편지를 받아보세요!
        </div>
      </v-card>
      <v-btn text color="secondary" class="mt-6" @click="shareKakao()">
        공유하기
      </v-btn>
    </v-col>

  </div>
</template>

<script>
import SHeader from '@/views/layout/header'
// import cardDetail from '@/views/main/components/cardDetail'
import { mdiCheck } from '@mdi/js'
import { kakaoShare } from '@/utils/share'

export default {
  name: 'Main',
  components: {
    SHeader,
    // cardDetail
  },
  filters: {
  },
  data () {
    return {
      icons: {
        mdiCheck
      },
      tinySliderOptions: {
        mouseDrag: true,
      },
      testList: [
        { "test": "test" },
        { "test": "test" },
        { "test": "test" },
        { "test": "test" },
      ]
    }
  },
  created () {
  },
  mounted() {
  },
  methods: {
    openDetail() {
      this.$refs.cardDetail.open()
    },
    shareKakao() {
      kakaoShare()
    },
  }
}
</script>

<style>
</style>