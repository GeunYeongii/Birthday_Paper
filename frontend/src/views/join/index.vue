<!--
  name : 이에닮
  desc : join
  date : 2022-01-05
-->
<template>
  <v-container>
    <s-header></s-header>
    <div class="join">

      <h1>회원가입</h1>

      <v-divider></v-divider>

      <v-row justify="center">
        <v-col cols="12">
          <v-card ref="form">
            <v-card-text>

              <form ref="joinForm">
                <v-row no-gutters>
                  <v-text-field
                    label="ID"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="PW"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="PW 체크"
                    :rules="rules"
                  ></v-text-field>
                </v-row>

                <v-row no-gutters>
                  <v-text-field
                    label="닉네임"
                    :rules="rules"
                  ></v-text-field>
                </v-row>
              </form>

            </v-card-text>

            <v-card-actions>
              <v-btn
                class="mauto"
                color="primary"
                @click="join()"
                rounded
                dark
              >
                회원가입
              </v-btn>
            </v-card-actions>
          </v-card>
          
        </v-col>
      </v-row>

    </div>
  </v-container>
</template>

<script>
import SHeader from '@/views/layout/header'

export default {
  name: 'Join',
  components: {
    SHeader
  },
  filters: {
  },
  data () {
    return {
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    join(){
      console.log('회원가입버튼')
    }
  }
}
</script>
