<!--
  name : 이예닮
  desc : 날짜선택 다이얼로그
  date : 2022-01-15
-->
<template>
  <v-dialog
    ref="dialog"
    v-model="visible"
    :return-value.sync="date"
    persistent
    width="290px"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
        v-model="date"
        :label="label"
        prepend-icon="mdi-calendar-month"
        readonly
        v-on="on"
        :rules="rules"
      ></v-text-field>
  </template>
    <v-date-picker v-model="date" :value="value" @input="getDate" :range="range" locale="ko" :allowed-dates="allowedDates" color="#474775">
      <v-spacer></v-spacer>
      <v-btn text color="primary" @click="visible = false">취소</v-btn>
      <v-btn text color="primary" @click="$refs.dialog.save(date)">확인</v-btn>
    </v-date-picker>
  </v-dialog>
</template>

<script>

export default {
  name: 'DatePicker',
  components: {
  },
  props: {
    // v-model로 들어오는 value
    value: {},
    // datePicker label
    label: String,
    // 시작 종료가 있는 달력 여부
    range: Boolean,
    // 유효성 검사
    rules: Array
  },
  filters: {
  },
  data () {
    return {
      visible: false,
      date: []
    }
  },
  methods: {
    getDate (date) {
      if(date.length > 1) {
        date.shift();
      }
      this.$emit('input', date[0])
    },
    allowedDates () {
      return true
    }
  }
}
</script>
<style>
.v-btn__content{
  font-size: 14px;
}
</style>
