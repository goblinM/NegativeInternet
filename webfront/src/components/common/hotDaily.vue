<template>
<el-container>
  <el-main>
    <div class="head-title">
      实时热点
    </div>
    <div class="table-box">
      <el-table :data="hotData">
        <el-table-column
          prop="rank"
          label="排名"
          align="center"
          width="200"
        >

        </el-table-column>
        <el-table-column
          prop="keyword"
          label="关键词"
          align="center"
          width="400"
        >
          <template slot-scope="scope">
            <!--{{scope.row.keyword}}-->
            <a :href='scope.row.keyword_link' target="_blank"><span>{{scope.row.keyword}}</span></a>
          </template>
        </el-table-column>
        <el-table-column
          label="相关链接"
          align="center"
          width="400"
          prop="news_link"
        >
          <template slot-scope="scope">
            <a target="_blank" :href="scope.row.news_link"><span style="padding: 15px auto">新闻</span></a>
            <a target="_blank" :href="scope.row.video_link"><span>视频</span></a>
            <a target="_blank" :href="scope.row.image_link"><span style="padding: 15px auto">图片</span></a>
        </template>
        </el-table-column>
        <el-table-column
          prop="search_score"
          label="搜索指数"
          align="center"
          width="200"
        >

        </el-table-column>
      </el-table>
    </div>
  </el-main>
</el-container>
</template>

<script>
    export default {
        name: "hotDaily",
        data(){
          return {
            // hotData:[
            //   {
            //     rank:"1",
            //     search_score:25464135,
            //     keyword:"鸡腿杀人",
            //     related_link:{
            //       news:"新闻",
            //       video:"视频",
            //       picture:"图片"
            //     }
            //   },

            // ],
            hotData:[],
            interVal: "",
          }
        },
      mounted(){
          this.refreshData();
      },
      created(){
        this.getHotData();
      },
      methods:{
          //获取数据
          getHotData(){
            this.$http({
              method:"GET",
              url:this.$store.state.location+"/api/hot/get_hot_data/",
               params: {}
            }).then((response)=>{
              let data = response.data;
              // console.log(data);
              this.hotData = data;
            }).catch(error=>{
              console.log(error)
            })
          },
          //轮询刷新爬虫热点数据
        refreshData(){
            let data = {
              "csrfmiddlewaretoken":this.getCookie('csrftoken'),
              "user_type":sessionStorage.getItem("user_type")
            };
            this.$http({
              method:"POST",
              url:this.$store.state.location+"/api/hot/start_hot_spider/",
              data:this.$Qs.stringify(data)
            }).then(response=>{
              let result = response.data;
              if(result === "ok"){
                console.log("refresh data ok");
                var _this = this;
                this.getHotData();
                this.interVal = setInterval(function () {
                  setTimeout(_this.refreshData(), 0)
                // _this.refreshData();
               }, 50000);
              }
              else{
                console.log("refresh data failed");
                this.$message.error({message: '热点数据更新失败！', duration: 700});
                clearInterval(this.interVal);
              }
            }).catch(error=>{
              this.$message.error({message: '热点数据更新失败！', duration: 700});
              clearInterval(this.interVal);
            })
        }
      }
    }
</script>

<style scoped>
.table-box{
  width: 1200px;
  margin: 20px auto;
}
.head-title{
    float: left;
    margin-left: 150px;
    margin-bottom: 15px;
    font-size: 20px;
}

</style>
