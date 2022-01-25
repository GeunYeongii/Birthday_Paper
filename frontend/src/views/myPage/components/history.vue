<!--
  name : 이에닮
  desc : history
  date : 2022-01-25
-->
<template>
  <div>
    <!-- 기능 공개 X 나중에 공개 -->
    <v-col cols="12" class="txtC_474775">
      <h6>Paper History</h6>
      <v-divider></v-divider>
      <v-hover class="mb-4" v-for="(history, index) in historyList" :key="index">
        <template v-slot:default="{ hover }">
          <v-card>
            <v-card-text>
              <span class="txtC_474775 history_title">{{history.year}}년도 에는 {{history.count}}명의 친구들이 편지를 보냈어요</span>
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
    </v-col>

    <s-confirm ref="confirm"></s-confirm>
    <s-spinner ref="spinner"></s-spinner>
  </div>
</template>

<script>
import { dateFormatter } from '@/utils/filters'
import { getHistoryList } from '@/api/history'

export default {
  name: 'MyPage',
  components: {
  },
  filters: {
    dateFormatter
  },
  data () {
    return {
      user:[],
      historyList: []
    }
  },
  created () {
  },
  mounted () {
    this.user = this.$store.state.user
    this.getHistoryList()
  },
  methods: {
    getHistoryList() {
      this.$refs.spinner.open()
      getHistoryList({idx : this.user.idx}).then(response => {
        this.$refs.spinner.close()
        if (response.code == 20000) {
          this.historyList = response.data
        } else {
          this.$refs.confirm.open('alert','카드정보 조회', response.message)
        }
      })
    },
    changePw() {

    },
    deleteUser() {
      
    }
  }
}
</script>
