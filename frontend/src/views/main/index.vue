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
      <v-card :class="totalCount | setMainCss" elevation="10">

        <div v-if="totalCount > 0">
          <div class="txtC_474775">
            <p class="pt-5 main_title p-0 m-0">♥ {{year}}년도에는 ♥</p>
            <p class="pt-0 main_title">♥ {{totalCount}}개의 편지가 도착했어요 ♥</p>
          </div>

          <v-card flat tile>
            <v-window v-model="pageKey">
              <v-window-item v-for="(letter, i) in letterList" :key="`card-${i}`">
                <v-col no-gutters cols="12" class="mt-2 pl-3 pr-3">
                  <v-row no-gutters>
                    <v-col class="d-inline-block"  v-for="(letter, j) in letter" :key="`card-list-${j}`" @click="openDetail(letter, j)">
                      <v-img :class="j | setCardDesign" max-width="100" width="16vw" :src="j | setCardSrc">
                        <div class="senderNm txtC_474775">{{letter.senderNm}}</div>
                      </v-img>
                    </v-col>
                  </v-row>
                </v-col>
              </v-window-item>
            </v-window>

            <v-card-actions class="justify-space-between">
              <v-btn text @click="prev">
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>
              
              <v-item-group v-model="pageKey" class="text-center" mandatory>
                <v-item v-for="k in totalPage" :key="`btn-${k}`" v-slot="{ active, toggle }">
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

    <card-detail ref="cardDetail"></card-detail>
    <s-confirm ref="confirm"></s-confirm>
    <s-spinner ref="spinner"></s-spinner>
  </div>
</template>

<script>
import SHeader from '@/views/layout/header'
import cardDetail from '@/views/main/components/cardDetail'

import { mdiCheck } from '@mdi/js'
import { kakaoShare } from '@/utils/share'
import { setMainCss, setCardDesign, setCardSrc } from '@/utils/filters'
import { getLetterList } from '@/api/letter'

export default {
  name: 'Main',
  components: {
    SHeader,
    cardDetail
  },
  filters: {
    setMainCss,
    setCardDesign,
    setCardSrc
  },
  data () {
    return {
      cardDetailDialog: true,
      letterList: [],
      totalCount: 0,
      totalPage: 0,
      pageKey: 0,
      /* icon */
      icons: {
        mdiCheck
      },
      year: new Date().getFullYear()
    }
  },
  created () {
  },
  mounted() {
    this.user = this.$store.state.user
    if (this.$route.params.year) {
      this.year = this.$route.params.year
    }
    this.getLetterList(this.year)
  },
  methods: {
    getLetterList(year) {
      this.$refs.spinner.open()
      getLetterList({ year : year }).then(response => {
        if (response.code == 20000) {
          this.totalPage = response.data.totalPage
          this.totalCount = response.data.totalCount
          this.letterList = response.data.letterList

          if (response.token){
            this.$store.dispatch('RefreshActoken', response.token)
          }
        } else if (response.code == 40000) {
          this.$store.dispatch('LogOut')
          this.$refs.confirm.open('alert','로그인 만료', response.message).then(() => {
            this.$router.push('/login')
          })
        } else {
          this.$refs.confirm.open('alert','카드정보 조회', response.message)
        }
        this.$refs.spinner.close()
      })
    },
    openDetail(letter, idx) {
      this.$refs.cardDetail.open(letter, idx)
    },
    shareKakao() {
      var shareData = {
        'nickname': this.user.nickname,
        'userIdx': this.user.idx
      }
      kakaoShare(shareData)
    },
    next () {
      this.pageKey = this.pageKey + 1 === this.totalPage ? 0 : this.pageKey + 1
    },
    prev () {
      this.pageKey = this.pageKey - 1 < 0 ? this.totalPage - 1 : this.pageKey - 1
    },
  }
}
</script>

<style>
.v-dialog,.v-dialog--active{
  box-shadow:none;
}
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