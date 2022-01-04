<template>
  <div class="header">
    <v-row no-gutters>
      <v-col cols="6">
        <v-img src="@/assets/img/logo_2.png" class="logo"></v-img>
      </v-col>

      <v-col cols="6">
        <v-img src="@/assets/img/menu.png" class="menu_icon"></v-img>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Header',
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
  },
  methods: {
  }
}
</script>

<style>
.header {
  height: 5rem;
}
.menu_icon{
  width: 15%;
  float: right;
  margin-top: 1.4rem;
  margin-right: 10px;
}
.logo {
  margin-top: 1.4rem;
  margin-left: 10px;
}
</style>
