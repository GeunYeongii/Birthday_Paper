<template>
  <div>
    테스트페이지1
  </div>
</template>

<script>
import { test1 } from "@/api/main";

export default {
  name: 'test1',
  components: {
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
    test1().then(response => {
      console.log(response)
    })
  },
  methods: {
  }
}
</script>
