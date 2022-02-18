<!--
  name : 이에닮
  desc : changePw
  date : 2022-01-07
-->
<template>
    <div class="changePw">
    <s-header></s-header>

</template>

<script>
import SHeader from '@/views/layout/header'

import { dateFormatter } from '@/utils/filters'

export default {
  name: 'changePw',
  components: {
    SHeader,
  },
  filters: {
    dateFormatter
  },
  data () {
    return {
        user:[],
        password: {
            old_password: '',
            new_password: '',
            repeat_password: ''
        }
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
