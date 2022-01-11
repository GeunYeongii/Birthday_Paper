<!--
  name : 이에닮
  desc : main
  date : 2022-01-05
-->
<template>
  <div class="main">
    <s-header></s-header>

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
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    openDetail() {
      this.$refs.cardDetail.open()
    },
    shareKakao() {
      kakaoShare()
    }
  }
}
</script>
