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
      <v-card class="m-auto main_card" elevation="10">

        <div v-if="length > 0">
          <div class="txtC_474775">
            <p class="pt-5">♥n개의 편지가 도착했어요♥</p>
          </div>

          <v-card flat tile>
            <v-window v-model="onboarding">
              <v-window-item v-for="n in length" :key="`card-${n}`">
                <div>
                  <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
                    <v-row no-gutters>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_4.png">
                          <div class="senderNm">이예닮</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft card_angle mt-3" max-width="90" width="16vw" src="@/assets/img/asset_3.png">
                          <div class="senderNm">주근영</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft" max-width="90" width="16vw" src="@/assets/img/asset_2.png">
                          <div class="senderNm">훈제족발</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_1.png">
                          <div class="senderNm">Gnyiii</div>
                        </v-img>
                      </v-col>
                    </v-row>
                  </v-col>
                  
                  <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
                    <v-row no-gutters>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_1.png">
                          <div class="senderNm">HunJeJugBal</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft mt-3" max-width="90" width="16vw" src="@/assets/img/asset_2.png">
                          <div class="senderNm">birthday paper</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft mt-1" max-width="90" width="16vw" src="@/assets/img/asset_4.png">
                          <div class="senderNm">bp</div>
                        </v-img>
                      </v-col>
                      <v-col class="d-inline-block">
                        <v-img class="m-auto shadow_eft card_angle" max-width="90" width="16vw" src="@/assets/img/asset_3.png">
                          <div class="senderNm">사용자</div>
                        </v-img>
                      </v-col>
                    </v-row>
                  </v-col>
                </div>

              </v-window-item>
            </v-window>

            <v-card-actions class="justify-space-between">
              <v-btn text @click="prev">
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              
              <v-item-group v-model="onboarding" class="text-center" mandatory>
                <v-item v-for="n in length" :key="`btn-${n}`" v-slot="{ active, toggle }">
                  <v-btn :input-value="active" icon @click="toggle">
                    <v-icon>mdi-record</v-icon>
                  </v-btn>
                </v-item>
              </v-item-group>

              <v-btn text @click="next">
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </div>

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
      // page수
      length: 5,
      // 현재 page 위치
      onboarding: 0,
    }
  },
  created () {
  },
  mounted() {
    this.getLetterList()
  },
  methods: {
    getLetterList() {
      /*
      로그인 한 사용자 id를 보내면 해당 유저의 letter List를 return 받아오는 api 호출
      
      [API return sample]
      {
        "letterList": [
          {
            "0": [
              { "idx": "0", "userNm": "test1" },
              { "idx": "1", "userNm": "test2" },
              { "idx": "2", "userNm": "test3" },
              { "idx": "3", "userNm": "test4" },
              { "idx": "4", "userNm": "test5" },
              { "idx": "5", "userNm": "test6" },
              { "idx": "6", "userNm": "test7" },
              { "idx": "7", "userNm": "test8" }
            ],
            "1": [
              { "idx": "8", "userNm": "test9" },
              { "idx": "9", "userNm": "test10" },
              { "idx": "10", "userNm": "test11" },
              { "idx": "11", "userNm": "test12" },
              { "idx": "12", "userNm": "test13" },
              { "idx": "13", "userNm": "test14" },
              { "idx": "14", "userNm": "test15" },
              { "idx": "15", "userNm": "test16" }
            ],
            "2": [
              { "idx": "16", "userNm": "test17" },
              { "idx": "17", "userNm": "test18" },
              { "idx": "18", "userNm": "test19" },
              { "idx": "19", "userNm": "test20" },
            ]
          }
        ],
        "totalCount": "20",
        "pageCount": "3"
      }

      letterList => 사용자가 받은 편지 List 3중배열
      totalCount => 사용자가 받은 편지 total count
      pageCount => 생성할 페이지 수

      */    
    },
    openDetail() {
      this.$refs.cardDetail.open()
    },
    shareKakao() {
      kakaoShare()
    },
    next () {
      this.onboarding = this.onboarding + 1 === this.length ? 0 : this.onboarding + 1
    },
    prev () {
      this.onboarding = this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1
    },
  }
}
</script>

<style>
.v-btn--icon.v-size--default {
  height: 20px;
  width: 20px;
}
.v-btn--icon.v-size--default .v-icon, .v-btn--fab.v-size--default .v-icon {
  height: 16px;
  font-size: 16px;
  width: 16px;
}
</style>