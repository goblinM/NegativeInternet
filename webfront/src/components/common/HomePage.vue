<template>
<div class="function-wrapper">
        <ul class="nav nav-tabs" role="tablist" id="pandect">
            <li role="presentation" :class="{active:shows==1}">
                <router-link target="_self" :to="{name:'hotDaily'}" @click="bindActive(1)"> <!--:to="{name:'hotDaily'}" -->
                    <!--<span class="icon-info-monitor-wrapper">-->
                    <!--<span class="icon-info-monitor"></span>-->
                    <img src="../../assets/1.png"/>
                    <span class="">每日热点</span>
                    <span class="ani_border"></span>
                    <!--</span>-->
                </router-link>
            </li>
            <li role="presentation" :class="{active:shows==2}">
                <router-link target="_self" :to="{name:'newsWatch'}" @click="bindActive(2)"> <!--:to="{name:'newsWatch'}" -->
                    <!--<span class="icon-info-warning"></span>-->
                  <img src="../../assets/2.png"/>
                    <span class="">资讯浏览</span>
                    <span class="ani_border"></span>
                </router-link>
            </li>
            <li role="presentation" :class="{active:shows==3}">
                 <router-link  target="_self" :to="{name:'dataAnalysis'}" @click="bindActive(3)">
                    <!--<span class="icon-info-analysis"></span>-->
                  <img src="../../assets/5.png"/>
                    <span class="">大数据分析</span>
                    <span class="ani_border"></span>
                 </router-link>
            </li>
            <li role="presentation" :class="{active:shows==4}">
                <router-link :to="{name:'#'}"  @click="bindActive(4)">
                    <!--<span class="icon-info-report"></span>-->
                  <img src="../../assets/3.png"/>
                    <span class="">用户管理</span>
                    <span class="ani_border"></span>
                </router-link>
            </li>
            <li role="presentation" :class="{active:shows==5}">
                <router-link :to="{name:'#'}"  @click="bindActive(5)">
                    <!--<span class="icon-info-screen"></span>-->
                  <img src="../../assets/4.png"/>
                    <span class="">爬虫管理</span>
                    <span class="ani_border"></span>
                </router-link>
            </li>
        </ul>
        <div class="bottom-wrap">
          <transition name="" mode="out-in">
          <router-view :key="routerActive"/>
        <!--<router-view v-else/>-->
          </transition>
      <!-- 尾部 -->
        </div>

    </div>
</template>

<script>
    export default {
        name: "HomePage",
        data(){
          return {
            routerActive:"",
            shows:1,
            urlData:[
              {
                name:"每日热点",
                url:"hotDaily"
              },
              {
                name:"资讯浏览",
                url:"newsWatch"
              },
              {
                name:"数据报告",
                url:"dataReport"
              },
              {
                name:"用户管理",
                url:"userManage"
              },
              {
                name:"爬虫管理",
                url:"spiderManage"
              }
            ]
          }
        },
      created(){},
      mounted(){},
      methods:{
          //点击tab栏动态添加active,这里似乎还需要考虑一下
          bindActive(cur){
            console.log(cur);
            this.shows = parseInt(cur);
            if(this.shows===1){
              this.$router.push({name:"/HomePage/hotDaily"});//跳转到index页面
            }
            else if(this.shows === 2){
              this.$router.push({name:"/HomePage/newsWatch"})
            }

          },
      },
    }
</script>

<style scoped>
  .bottom-wrap{
    min-height: 500px;
    background: #f5f7fa;
    /*border: 1px solid darkred;*/
    top: 246px;
    position: relative;
  }
.function-wrapper{
  position:relative;height:246px;
  background:url(../../assets/nav_banner.jpg) no-repeat center center;
  background-size:cover;
}
.function-wrapper ul li {
    display: inline-block;
    width: 20%;
    text-align: center;
    font-size: 14px;
}
.function-wrapper ul {
    border: none;
    position: absolute;
    bottom: 0;
    padding: 0 130px;
    width: 83%;
    font-size: 0;
}

.function-wrapper ul li a span:first-child {
    margin-bottom: 5px;
    color: #fff;
    font-size: 25px;
}
.function-wrapper ul li a span {
    display: block;
      color: white;
}
.function-wrapper ul li.active a span:first-child {
    color: #3fc3e3;
}


.function-wrapper ul li a:hover span:first-child, .nav-tabs>li.active>a span, .nav-tabs>li.active>a:focus span, .nav-tabs>li.active>a:hover span {
    /*color: #3fc3e3;*/
     border-bottom: 3px solid #1e6c95;
}

</style>
