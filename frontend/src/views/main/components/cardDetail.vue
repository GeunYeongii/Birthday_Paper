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
          <h6>{{senderNm}} 님이 보낸 편지입니다</h6>
          
            <p v-html="letterContents"></p>
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
          <h6>{{senderNm}} 님이 보낸 편지입니다</h6>
          
            <p v-html="letterContents"></p>
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
          <h6>{{senderNm}} 님이 보낸 편지입니다</h6>
          
            <p v-html="letterContents"></p>
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
          <h6>{{senderNm}} 님이 보낸 편지입니다</h6>
          
            <p v-html="letterContents"></p>
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
      senderNm:'',
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
      this.senderNm = letter.senderNm
      this.letterContents = letter.letterContent.replace(/\n/g, "<br />")
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