<template>
  <div>
    테스트페이지2
  </div>
</template>

<script>
import { test2 } from "@/api/main";

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
  }
}
</script>
