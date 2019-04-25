<template>
  <el-container>
    <el-main>
      <div class="table-box layout-frame">
        <div class="condition-setting">
          <div class="setting-line font-size-0 pt0">
            <div class="inline-block font-size-0 left-setting">
              <div class="inline-block setting-name"><span class="">监测时间:</span>
              </div>
              <ul class="setting-tools font-size-0 inline-block">
                <li>
                  <span class="">今天</span>
                </li>
                <li class="active">
                  <span class="">24小时</span>
                </li>
                <li class="">
                  <span class="">2天</span>
                </li>
                <li class="">
                  <span class="">3天</span>
                </li>
                <li class="">
                  <span class="">7天</span>
                </li>
                <li class="">
                  <span class="">10天</span>
                </li>
                <li class="">
                  <span class="">自定义</span>
                </li>
              </ul>
            </div>
            <div class="inline-block font-size-0 right-setting">
              <div class="inline-block setting-name"><span class="">信息排列:</span>
              </div>
              <ul class="setting-tools font-size-0 inline-block" id="dateTime">

                <li id="dateTimeA_1" class="active">
                  <span class="">时间降序</span>
                </li>
                <li id="dateTimeA_2">
                  <span class="">时间升序</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="hidden-wrapper">
            <div class="setting-line font-size-0">
              <div class="inline-block font-size-0 left-setting">
                <div class="inline-block setting-name"><span class="">信息属性:</span></div>
                <ul class="setting-tools font-size-0 inline-block" id="attribute">
                  <li id="attributeA_1" class="active" >
                    <span class="">全部</span>
                  </li>
                  <li id="attributeA_2">
                    <span class="">敏感</span>
                  </li>
                  <li id="attributeA_3">
                    <span class="">非敏感</span>
                  </li>
                </ul>
              </div>
              <div class="inline-block font-size-0 right-setting">
                <div class="inline-block setting-name"><span class="">匹配方式:</span></div>
                <ul class="setting-tools font-size-0 inline-block" id="matchTypes">
                  <li id="matchTypeA_1" class="active" >
                    <span class="">按全文</span>
                  </li>
                  <li id="matchTypeA_2" class="">
                    <span class="">按标题</span>
                  </li>
                  <li id="matchTypeA_3" class="">
                    <span class="">按正文</span>
                  </li>

                </ul>
              </div>

            </div>
            <div class="setting-line font-size-0">
              <div class="inline-block font-size-0  left-setting">
                 <div class="inline-block setting-name"><span class="">信息种类:</span></div>
                <ul class="setting-tools font-size-0 inline-block" id="dataType">
                  <li id="dataType_1" class="active" >
                    <span class="">全部</span>
                  </li>
                  <li id="dataType_2" class="">
                    <span class="">金融</span>
                  </li>
                  <li id="dataType_3" class="">
                    <span class="">政治</span>
                  </li>
                  <li id="dataType_4" class="">
                    <span class="">娱乐</span>
                  </li>
                  <li id="dataType_5" class="">
                    <span class="">科技</span>
                    <li id="dataType_6" class="">
                    <span class="">社会</span>
                  </li>
                  <li id="dataType_7" class="">
                    <span class="">文化</span>
                  </li>

                </ul>
               </div>
              <div class="inline-block font-size-0  right-setting"></div>

            </div>

          </div>
        </div>
      </div>
      <div class="table-box">
        <el-table :data="hotData">
          <el-table-column
            prop="id"
            label="序号"
            align="center"
            width="50"
          >
          </el-table-column>
          <el-table-column
            prop="title"
            label="标题"
            align="center"
            width="300"
          >
          </el-table-column>
          <el-table-column
            prop="describe"
            label="描述"
            align="center"
            width="350"
          >
          </el-table-column>
          <el-table-column
            prop="keyword"
            label="关键词"
            align="center"
            width="150"
          >
          </el-table-column>
          <el-table-column
            prop="data_source"
            label="数据来源"
            align="center"
            width="100"
          >
          </el-table-column>
          <el-table-column
            prop="similar_news"
            label="相似文章"
            align="center"
            width="100"
          >
          </el-table-column>
          <el-table-column
            prop="pub_time"
            label="报告时间"
            align="center"
            width="150"
          >
          </el-table-column>
        </el-table>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "newsWatch",
    data() {
      return {
        hotData: [
          {
            id: "1",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: "1"
          },
          {
            id: "2",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: 1
          },
          {
            id: "3",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: 1
          },
          {
            id: "4",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: 1
          },
          {
            id: "5",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: 1
          },
          {
            id: "6",
            title: "历史转折中的刘强东",
            keyword: "京东 中关村 北京 人家 东哥",
            pub_time: "2018-12-24 19:09",
            data_source: "叉烧往事",
            describe: "011993年，凭借一曲《把根留住》，台湾歌手童安格获得“中国十大受欢迎歌手奖”。不知是不是“把根留住”四个字击中了刘强东",
            similar_news: 1
          },


        ]
      }
    },
  }
</script>

<style scoped>
  .setting-line .setting-tools>li.active span {
    background-color: #47c3e1;
    color: #fff;
}
  .layout-frame {
    padding: 10px;
    background-color: #fff;
    box-shadow: 0 1px 6px 0 rgba(136, 157, 175, .3);
    color: black;

  }

  .table-box {
    width: 1200px;
    margin: 20px auto;
  }

  .setting-line {
    padding: 10px 0;
    border-bottom: 1px solid #e6e6e6;
  }

  .font-size-0 {
    font-size: 0 !important;
  }

  .pt0 {
    padding-top: 0 !important;
  }

  .font-size-0 > .inline-block {
    vertical-align: top;
    font-size: 13px;
  }

  .inline-block {
    display: inline-block;
  }

  .setting-line .left-setting, .setting-line .right-setting {
    width: 50%;
  }

  .setting-line .right-setting {
    width: 50%;
  }

  .setting-line .setting-name {
    width: 70px;
    color: #999;
    vertical-align: top;
    text-align: left;
    font-size: 13px;
  }

  .setting-line .setting-tools {
    width: calc(100% - 70px);
    vertical-align: top;
  }

  .setting-line .setting-tools > li {
    display: inline-block;
    padding-right: 15px;
    color: #333;
    text-align: left;
    font-size: 13px;
  }

  .setting-line .setting-tools > li span {
    display: block;
    padding: 1px 5px;
    -webkit-transition: all .2s;
    transition: all .2s;
  }

  ul.font-size-0 li {
    display: inline-block;
    vertical-align: top;
    font-size: 14px;
    text-align: center;
    position: relative;
  }

  li, ul {
    margin: 0;
    padding: 0;
    border: none;
    list-style: none;
  }
</style>
