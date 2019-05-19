<template>
  <el-container>
    <el-main>
      <div class="analysis-global-wrapper">
        <div class="analysis-global">
          <div class="analysis-title module-title">
            <span class="">全网事件分析</span>
          </div>
          <div class="analysis-desc">
            <p class="">
              对某一网络事件在互联网上的整体传播情况，收集全网数据进行分析，自动生成涵盖事件简介、事件走势、网站统计、数据类型、关键词云、热门信息、热点网民、传播路径、相关词、网民观点、舆情总结等11个维度的全网事件分析报告。
            </p>
            <p class="">
              <span class="dot mr5"></span>通过全网事件分析，可以快速找出某个网络事件的信息传播源头。
            </p>
          </div>
          <div class="image-desc-wrapper">
            <img src="../../assets/global-analysis.png" alt="">
          </div>
          <div class="showcase-wrapper">
            <ul class="font-size-0">
              <li class="part-three pr20">
                <router-link
                  :to="'/dataReport/zhihu_icu/'"
                  target="_blank">
                  <div class="case-desc-image no-pics">
                    <img src="../../assets/996icusmall.jpg" alt="996icu">
                  </div>
                </router-link>
                <div class="case-desc-title pr20">
                  <span><router-link :to="'/dataReport/zhihu_icu/'" target="_blank" style="color: #fff" >案例展示</router-link></span>
                </div>
              </li>
              <li class="part-three pr10 pl10">
                <router-link :to="'/dataReport/zhihu_paris/'"
                  target="_blank">
                  <div class="case-desc-image no-pics">
                    <img src="../../assets/parissmall.jpg" alt="hire_paris">
                  </div>
                </router-link>
                <div class="case-desc-title">
                  <span><router-link :to="'/dataReport/zhihu_paris/'"
                    target="_blank" style="color: #fff">案例展示</router-link></span>
                </div>
              </li>
              <li class="part-three pl20">
                <router-link :to="'/dataReport/zhihu_car/'" target="_blank">
                  <div class="case-desc-image no-pics">
                    <img src="../../assets/benchismall.jpg" alt="奔驰">
                  </div>
                </router-link>
                <div class="case-desc-title pr20">
                  <span><router-link  :to="'/dataReport/zhihu_car/'"
                    target="_blank" style="color: #fff">案例展示</router-link></span>
                </div>
              </li>
            </ul>
          </div>


        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "dataAnalysis",
    data(){
      return {

      }
    },
    mounted(){},
    created(){},
    methods:{
      // GetReport(data_name,keywords){
      //   let data = {
      //     "data_name": data_name,
      //     "keywords": keywords,
      //     "csrfmiddlewaretoken": this.getCookie('csrftoken')
      //   };
      //   this.$http({
      //       url: this.$store.state.location + "/api_report/",
      //       method: "POST",
      //       data: this.$Qs.stringify(data),
      //   }).then(response =>{
      //     let result = response.data;
      //     console.log(result['data'])
      //   }).catch(error =>{
      //     console.log(error);
      //   })
      // }
    },

  }
</script>

<style scoped>
.module-title {
    text-align: center;
    font-size: 24px;
    letter-spacing: 0.03em;
    color: #494c52;
    margin: 30px 0;
}
  .analysis-title .dot-wrapper {
    height: 20px;
    line-height: 20px;
}
  .analysis-desc {
    font-size: 12px;
    line-height: 1.8;
    color: #999;
    text-align: center;
}
  .image-desc-wrapper {
    text-align: center;
    margin: 30px 0;
    width: auto;
}

.showcase-wrapper {
    /*margin: 15px 0;*/
    text-align: center;
    font-size: 13px;
  margin: 50px 0 40px;
}
  .font-size-0 {
    font-size: 0!important;
}
li, ul {
    margin: 0;
    padding: 0;
    border: none;
    list-style: none;
}
  ul.font-size-0 li.part-three {
    width: 33.33%;
}
ul.font-size-0 li {
    display: inline-block;
    vertical-align: top;
    font-size: 14px;
    text-align: center;
    position: relative;
  padding: 0;
}
.pr20 {
    padding-right: 20px;
}
.pl10 {
    padding-left: 10px;
}
  .pl20 {
    padding-left: 20px;
}
  .case-desc-title {
    position: absolute;
    width: 100%;
    bottom: -19px;
    cursor: pointer;
}
  a {
    color: #337ab7;
    text-decoration: none;
}
a {
    background-color: transparent;
}
  .case-desc-image {
    width: 100%;
    padding: 0;
    height: 140px;
    overflow: hidden;
}
  .case-desc-title {
    position: absolute;
    width: 100%;
    bottom:  -60px;
    cursor: pointer;
}
  .case-desc-title span {
    padding: 6px 20px;
    background-color: #3fc3e3;
    color: #fff;
    display: inline-block;
    border-radius: 3px;
}
</style>
