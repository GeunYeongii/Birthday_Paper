<!--
  name : 이에닮
  desc : Header
  date : 2022-01-04
-->
<template>
  <div class="header">
    <v-row no-gutters class="text-center mt-2">
      <v-col cols="8" offset="2" @click="goMain()">
        <p class="h6 text_logo mt-5 txtC_474775">BIRTHDAY PAPER</p>
      </v-col>
      <v-col cols="2">
        <v-app-bar-nav-icon class="nav_icon menu_icon txtC_474775" x-large @click="toggleDialog()"></v-app-bar-nav-icon>
      </v-col>
    </v-row>

    <v-navigation-drawer
      v-model="menuDialog"
      absolute
      temporary
    >
      <v-row no-gutters class="text-center mt-2">
        <v-col cols="12">
          <p class="h6 text_logo mt-5 txtC_474775" @click="goMain()">BIRTHDAY PAPER</p>

          <v-img class="profile_img mt-1" src="https://randomuser.me/api/portraits/men/78.jpg" @click="goMyPage()"></v-img>
          <p class="h6 profile_name txtC_474775" @click="goMyPage()">000 님</p>

          <v-btn text color="secondary" @click="logout()">
            로그아웃
          </v-btn>
        </v-col>
      </v-row>

      <v-divider class="menu_divider"></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          @click="clickMenu(item)"
          link
        >
          <v-list-item-icon class="mr-0">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content class="ms-2">
            <v-list-item-title class="text-gray">{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

    </v-navigation-drawer>
  </div>
</template>

<script>

export default {
  name: 'Header',
  components: {
  },
  data () {
    return {
      menuDialog: false,
      items: [
        { icon: 'mdi-circle-small', title: '메인화면', path: '/main' },
        { icon: 'mdi-circle-small', title: '공지사항', path: '/notice' },
        { icon: 'mdi-circle-small', title: 'Introduce', path: '/introduce' },
      ],
    }
  },
  methods: {
    goMain() {
      this.$router.push('/main').catch(() => {})
    },
    goMyPage() {
      this.$router.push('/myPage').catch(() => {})
    },
    clickMenu(item) {
      if(this.$route.path!==item.path) {
        this.$router.push(item.path)
      } else {
        this.toggleDialog()
      }
    },
    logout() {
      console.log('로그아웃버튼')
    },
    toggleDialog() {
      this.menuDialog = !this.menuDialog
    }
  }
}
</script>

<style>
.menu_divider{
  margin-top:0.5rem;
  margin-bottom:0rem;
}
</style>
