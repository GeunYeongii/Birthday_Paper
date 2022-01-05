<!--
  name : 이에닮
  desc : Header
  date : 2022-01-04
-->
<template>
  <div class="header">
    <v-row no-gutters class="mt-3 mb-2">
      <v-col cols="9">
        <v-img
        contain
        max-height="65"
        max-width="250"
        @click="goMain()"
        src="@/assets/img/logo_2.png"></v-img>
      </v-col>
      <v-col cols="3">
        <v-app-bar-nav-icon class="nav_icon mt-1" @click="toggleDialog()"></v-app-bar-nav-icon>
      </v-col>
    </v-row>

    <v-navigation-drawer
      v-model="menuDialog"
      absolute
      temporary
    >
      <v-list-item>
        <v-img
          @click="goMain()"
          src="@/assets/img/logo_2.png" class="mt-4">
        </v-img>
      </v-list-item>
      
      <v-list-item>
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-row no-gutters>
            <v-col cols="6">
              <v-list-item-title class="text-gray">OOO 님</v-list-item-title>
            </v-col>
            <v-col cols="6">
              <v-btn color="primary" @click="logout()" small rounded dark elevation="3">
                로그아웃
              </v-btn>
            </v-col>
          </v-row>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          @click="clickMenu(item)"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content class="ms-2">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
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
        { icon: 'mdi-access-point', title: '메인화면', path: '/main' },
        { icon: 'mdi-access-point', title: '공지사항', path: '/notice' },
      ],
    }
  },
  methods: {
    goMain() {
      this.$router.push('/')
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
.nav_icon{
  float: right;
}
</style>
