<template>
  <div>
    테스트페이지2
    <button type="button" @click="clickTest()">
    test
    </button>
  </div>
</template>

<script>
import { test2, test3 } from "@/api/main";

export default {
  name: 'test2',
  components: {
  },
  filters: {
  },
  data () {
    return {
    }
  },
  created () {
    test2().then(response => {
      console.log(response)
    })
  },
  mounted () {
  },
  methods: {
    clickTest() {
      console.log('clickTest 함수 실행')
      let test = '데이터 전송 테스트'
      test3(test).then(response => {
        console.log(response)
      })
    }
  }
}
</script>
