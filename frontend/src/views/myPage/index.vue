<!--
  name : 이에닮
  desc : myPage
  date : 2022-01-07
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="myPage">

      <h2 class="text-gray">MyPage</h2>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">

          <v-card elevation="0" class="">
            <v-card-actions bottom>
              <div class="mauto">
                <v-list-item-avatar size="100" class="mauto">
                  <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
                </v-list-item-avatar>
              </div>
            </v-card-actions>
          </v-card>

        </v-col>

        <v-col cols="6">
          <v-card>
            <v-list-item three-line>
              <v-list-item-content>
                <v-list-item-title class="mb-1">
                  닉네임
                </v-list-item-title>
                <v-list-item-subtitle>
                  훈제족발
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>

        <v-col cols="6">
          <v-card>
            <v-list-item three-line>
              <v-list-item-content>
                <v-list-item-title class="mb-1">
                  생년월일
                </v-list-item-title>
                <v-list-item-subtitle>
                  1998-05-04
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>

        <v-col cols="12">
          <h4>Paper History</h4>
          <v-divider></v-divider>
          <v-hover class="mb-4">
            <template v-slot:default="{ hover }">
              <v-card>
                <v-card-text>
                  <span>2021년도 에는 34명의 친구들이 편지를 보냈어요</span>
                </v-card-text>
                
                <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#036358"
                  >
                    <v-btn>편지 읽으러 가기</v-btn>
                  </v-overlay>
                </v-fade-transition>

              </v-card>
            </template>
          </v-hover>

          <v-hover class="mb-4">
            <template v-slot:default="{ hover }">
              <v-card>
                <v-card-text>
                  <span>2020년도 에는 17명의 친구들이 편지를 보냈어요</span>
                </v-card-text>
                
                <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#036358"
                  >
                    <v-btn>편지 읽으러 가기</v-btn>
                  </v-overlay>
                </v-fade-transition>

              </v-card>
            </template>
          </v-hover>

          <v-hover class="mb-4">
            <template v-slot:default="{ hover }">
              <v-card>
                <v-card-text>
                  <span>2019년도 에는 28명의 친구들이 편지를 보냈어요</span>
                </v-card-text>
                
                <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#036358"
                  >
                    <v-btn>편지 읽으러 가기</v-btn>
                  </v-overlay>
                </v-fade-transition>

              </v-card>
            </template>
          </v-hover>

        </v-col>

        <v-card elevation="0" class="">
          <v-card-actions bottom>
            <div class="mauto">
              <v-btn color="primary" dark @click="changePw()">
                PW 변경
              </v-btn>
              <v-btn class="ml-4" color="primary" dark @click="deleteUser()">
                회원탈퇴
              </v-btn>
            </div>
          </v-card-actions>
        </v-card>

      </v-row>

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'MyPage',
  components: {
    SHeader,
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
    changePw() {

    },
    deleteUser() {
      
    }
  }
}
</script>
