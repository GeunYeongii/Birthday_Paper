<!--
  name : 이에닮
  desc : cardDetail
  date : 2022-01-05
-->
<template>
  <div>
    <v-dialog max-width="550" v-model="cardDetailDialog1" content-class="elevation-0">
      <v-img src="@/assets/img/asset_5.png">
        <div class="text-center cardDetail txtC_474775">
          <h6>{{userName}} 님이 보낸 편지입니다</h6>
          
          <p>
            {{letterContents}}
          </p>
        </div>
        
        <v-col no-gutters cols="12" class="cardDetail-footer text-center">
          <v-btn text color="secondary" class="" @click="close()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>
    
    <v-dialog max-width="550" v-model="cardDetailDialog2" content-class="elevation-0">
      <v-img src="@/assets/img/asset_6.png">
        <div class="text-center cardDetail txtC_474775">
          <h6>{{userName}} 님이 보낸 편지입니다</h6>
          
          <p>
            {{letterContents}}
          </p>
        </div>
        
        <v-col no-gutters cols="12" class="cardDetail-footer text-center">
          <v-btn text color="secondary" class="" @click="close()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>
    
    <v-dialog max-width="550" v-model="cardDetailDialog3" content-class="elevation-0">
      <v-img src="@/assets/img/asset_7.png">
        <div class="text-center cardDetail txtC_474775">
          <h6>{{userName}} 님이 보낸 편지입니다</h6>
          
          <p>
            {{letterContents}}
          </p>
        </div>
        
        <v-col no-gutters cols="12" class="cardDetail-footer text-center">
          <v-btn text color="secondary" class="" @click="close()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>
    
    <v-dialog max-width="550" v-model="cardDetailDialog4" content-class="elevation-0">
      <v-img src="@/assets/img/asset_8.png">
        <div class="text-center cardDetail txtC_474775">
          <h6>{{userName}} 님이 보낸 편지입니다</h6>
          
          <p>
            {{letterContents}}
          </p>
        </div>
        
        <v-col no-gutters cols="12" class="cardDetail-footer text-center">
          <v-btn text color="secondary" class="" @click="close()">
            확인
          </v-btn>
        </v-col>

      </v-img>
    </v-dialog>
  </div>
</template>

<script>

export default {
  name: 'CardDetail',
  components: {
  },
  filters: {
  },
  data () {
    return {
      userName:'',
      letterContents:'',
      cardDetailDialog1: false,
      cardDetailDialog2: false,
      cardDetailDialog3: false,
      cardDetailDialog4: false,
    }
  },
  created () {
  },
  mounted () {
  },
  methods: {
    open(letter,idx) {
      this.openDialog(idx)
      var data = {
        letterContents: "1월9일 생일 진심으로 축하해! 너랑 모든 순간이 행복했고, 함께해준 너에게 항상 고마워 :) 오늘은 맛있는것도 많이 먹고, 좋은 사람들과 즐거운 시간 보내면서 누구보다 행복했으면 좋겠다. 너를 언제나 응원하고 있어! 생일축하하고, 항상 행복한 하루 보내길 바래♥"
      }
      this.userName = letter.userNm
      this.letterContents = data.letterContents
    },
    close() {
      this.cardDetailDialog1= false
      this.cardDetailDialog2= false
      this.cardDetailDialog3= false
      this.cardDetailDialog4= false
    },
    openDialog(idx) {
      switch(idx) {
        case 0:
        case 6:
          this.cardDetailDialog4 = true
          break
        case 1:
        case 7:
          this.cardDetailDialog3 = true
          break
        case 2:
        case 5:
          this.cardDetailDialog2 = true
          break
        case 3:
        case 4:
          this.cardDetailDialog1 = true
          break
      }
    }
  }
}
</script>

<style>
.transparent {
   background-color: white!important;
   opacity: 0.65;
   border-color: transparent!important;
 }
</style>