<!--
  name : 이에닮
  desc : myPage
  date : 2022-01-07
-->
<template>
    <div class="myPage">
    <s-header></s-header>

    <h6 class="text-center txtC_474775 mt-6">MyPage</h6>

    <v-divider></v-divider>

    <v-row justify="center" class="ml-4 mr-4">
      <v-col cols="12">
        <v-img class="mypage_profile mt-1" src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
      </v-col>

      <v-col cols="6">
        <v-card>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="mb-1 txtC_474775">
                닉네임
              </v-list-item-title>
              <v-list-item-subtitle>
                <span class="txtC_474775">{{user.nickname}}</span>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>

      <v-col cols="6">
        <v-card>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="mb-1 txtC_474775">
                생년월일
              </v-list-item-title>
              <v-list-item-subtitle>
                <span class="txtC_474775">{{user.birth | dateFormatter}}</span>
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>

      <!-- 기능 공개 X 나중에 공개 -->
      <!-- <v-col cols="12" class="txtC_474775">
        <h6>Paper History</h6>
        <v-divider></v-divider>
        <v-hover class="mb-4">
          <template v-slot:default="{ hover }">
            <v-card>
              <v-card-text>
                <span class="txtC_474775 history_title">2021년도 에는 34명의 친구들이 편지를 보냈어요</span>
              </v-card-text>
                
              <v-fade-transition>
                <v-overlay
                  v-if="hover"
                  absolute
                  color="#474775"
                >
                  <v-btn>편지 읽으러 가기</v-btn>
                </v-overlay>
              </v-fade-transition>

            </v-card>
          </template>
        </v-hover>
      </v-col> -->
      
      <v-col cols="12" class="text-center">

        <v-btn color="secondary" dark @click="changePw()">
          PW 변경
        </v-btn>
        <v-btn class="ml-4" color="secondary" dark @click="deleteUser()">
          회원탈퇴
        </v-btn>
      </v-col>

    </v-row>

  </div>
</template>

<script>
import SHeader from '@/views/layout/header'
import { dateFormatter } from '@/utils/filters'

export default {
  name: 'MyPage',
  components: {
    SHeader,
  },
  filters: {
    dateFormatter
  },
  data () {
    return {
      user:[]
    }
  },
  created () {
  },
  mounted () {
    this.user = this.$store.state.user
  },
  methods: {
    changePw() {

    },
    deleteUser() {
      
    }
  }
}
</script>
