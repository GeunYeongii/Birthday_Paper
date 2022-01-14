<!--
  name : 이에닮
  desc : notice
  date : 2022-01-05
-->
<template>
  <div class="introduce">
    <s-header></s-header>

    <h6 class="text-center txtC_474775 mt-6">introduce</h6>

    <v-divider></v-divider>

    <v-row justify="center" class="ml-4 mr-4 text-center">

      <v-col cols="12" class="txtC_474775">
        <h6>제작자</h6>
        <v-divider></v-divider>

        <v-card class="mx-auto" outlined>
          <v-list-item three-line>
            <v-img
              class="introduce_img mt-2 mb-2"
              src="https://randomuser.me/api/portraits/men/78.jpg">
            </v-img>
            <v-list-item-title class="text-h6 mb-2 txtC_474775">
              <div class="text-overline mb-2 txtC_474775">
                디자이너
              </div>
              김정화
            </v-list-item-title>
          </v-list-item>
        </v-card>

        <v-card class="mx-auto mt-4" outlined>
          <v-list-item three-line>
            <v-img
              class="introduce_img mt-2 mb-2"
              src="https://randomuser.me/api/portraits/men/78.jpg">
            </v-img>
            <v-list-item-title class="text-h6 mb-2 txtC_474775">
              <div class="text-overline mb-2 txtC_474775">
                퍼블리싱 | Front | Back
              </div>
              이예닮
            </v-list-item-title>
          </v-list-item>
        </v-card>

        <v-card class="mx-auto mt-4" outlined>
          <v-list-item three-line>
            <v-img
              class="introduce_img mt-2 mb-2"
              src="https://randomuser.me/api/portraits/men/78.jpg">
            </v-img>
            <v-list-item-title class="text-h6 mb-2 txtC_474775">
              <div class="text-overline mb-2 txtC_474775">
                Back
              </div>
              주근영
            </v-list-item-title>
          </v-list-item>
        </v-card>

      </v-col>

      <v-col cols="12" class="txtC_474775">
        <h6>후원</h6>
        <v-divider></v-divider>
        <p>0000000000000000</p>
      </v-col>

    </v-row>

  </div>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'Introduce',
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
