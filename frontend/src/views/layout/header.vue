<!--
  name : 이에닮
  desc : Header
  date : 2022-01-04
-->
<template>
  <div class="header">
    <v-row no-gutters>
      <v-col cols="6">
        <v-img src="@/assets/img/logo_2.png" class="logo" @click="clickLogo()"></v-img>
      </v-col>
      <v-col cols="6">
        <v-img src="@/assets/img/menu.png" class="menu_icon" @click="clickMenu()"></v-img>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Header',
  methods: {
    clickLogo () {
      this.$router.push("main")
    },
    clickMenu () {
      console.log('메뉴클릭')
    }
  }
}
</script>

<style>
.header {height: 5rem;}
.logo {margin-top: 1.4rem; margin-left: 10px;}
.menu_icon{width: 15%; float: right; margin-top: 1.4rem; margin-right: 10px;}
</style>
