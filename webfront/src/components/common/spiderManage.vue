<template>
  <el-container>
    <el-main>
      <div class="head-title" style="float: left;margin-top: 50px;margin-left: 110px;">
        <el-button class="btn-primary" @click="StartSpider('start')" :type="start_color">
          启动爬虫
        </el-button>
      </div>
      <div class="head-title" style="float: left;margin-top: 50px;margin-left: 110px;" >
        <el-button class="btn-primary" @click="EndSpider('end')" :type="stop_color">
          停止爬虫
        </el-button>
      </div>
      <div class="start_son" v-if="start_flag === true" style="float: right;margin-right: 100px;margin-top: 50px;">
        <el-button class="btn-primary" @click="send_spider('hotdaily')">每日热点爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_financial')">金融爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_social')">社会爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_culture')">文化爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_science')">科技爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_amusement')">娱乐爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_gov')">政治爬虫</el-button>
      </div>

      <div class="end_son" v-if="stop_flag === true" style="float: right;margin-right: 100px;margin-top: 50px;">
        <el-button class="btn-primary" @click="send_spider('hotdaily')">每日热点爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_financial')">金融爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_social')">社会爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_culture')">文化爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_science')">科技爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_amusement')">娱乐爬虫</el-button>
        <el-button class="btn-primary" @click="send_spider('chinanews_gov')">政治爬虫</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "spiderManage",
    data() {
      return {
        start_flag: false,
        stop_flag: false,
        spider_type: "",
        start_color:"",
        stop_color:""
      }
    },
    mounted() {
    },
    created() {
    },
    methods: {
      StartSpider(cur) {
        this.spider_type = cur;
        this.start_flag = true;
        this.stop_flag = false;
        this.start_color = "success";
        this.stop_color = "default";
      },
      EndSpider(cur) {
        this.spider_type = cur;
        this.stop_flag = true;
        this.start_flag = false;
        this.stop_color = "success";
        this.start_color = "default";
      },
      send_spider(cur){
        console.log(cur);
        let data = {
          "spider_name":cur,
          "spider_type":this.spider_type,
          "csrfmiddlewaretoken":this.getCookie('csrftoken'),
        };
        this.$http({
            method:"post",
            url:this.$store.state.location+"/api_spider/",
            data: this.$Qs.stringify(data)
        }).then(response=>{
            let result = response.data;
            if(result === 'ok'){
              this.$message({
                type:"success",
                message:"操作成功"
              })
            }
            else{
              this.$message({
                type:"success",
                message:"操作失败"
              })
            }
        }).catch(error =>{
          console.log(error);
        })
      }
    }
  }

</script>

<style scoped>

</style>
