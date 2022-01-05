<template>
  <v-container>
    <s-header></s-header>
    <div class="notice">

      <h1>공지사항</h1>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">
          <v-expansion-panels>
            <v-expansion-panel
              v-for="(item,i) in 5"
              :key="i"
            >
              <v-expansion-panel-header>
                Item
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'Notice',
  components: {
    SHeader
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
