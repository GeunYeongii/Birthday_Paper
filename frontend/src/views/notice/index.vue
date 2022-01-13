<!--
  name : 이에닮
  desc : notice
  date : 2022-01-05
-->
<template>
  <div class="notice">
    <s-header></s-header>

    <h6 class="text-gray text-center txtC_474775 mt-6">공지사항</h6>

    <v-divider></v-divider>

    <v-row justify="center">
      <v-col cols="12">

        <v-card class="ml-6 mr-6" elevation="1">
          <v-expansion-panels>
            <v-expansion-panel
              v-for="(item,i) in 5"
              :key="i"
            >
              <v-expansion-panel-header class="txtC_474775">
                Item
              </v-expansion-panel-header>
              <v-expansion-panel-content class="txtC_474775">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-col>
    </v-row>

  </div>
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
