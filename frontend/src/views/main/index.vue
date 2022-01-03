<template>
  <div>
    메인페이지
  </div>
</template>

<script>
import { main } from "@/api/main";

export default {
  name: 'main',
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
    main().then(response => {
      console.log(response)
    })
  },
  methods: {
  }
}
</script>
