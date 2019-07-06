<template>
  <el-container>
    <el-main>
      <div class="page-container reportWeb rel">
        <ul id="nav2">
          <li id="r1" @click="onePageNav('1')" :class="{'current':liselected=== '1'}"><a href="#pr1">评论统计</a></li>
          <li id="r2" @click="onePageNav('2')" :class="{'current':liselected=== '2'}"><a href="#pr2">点赞统计</a></li>
          <li id="r3" @click="onePageNav('3')" :class="{'current':liselected=== '3'}"><a href="#pr3">男女比例</a></li>
          <li id="r4" @click="onePageNav('4')" :class="{'current':liselected=== '4'}"><a href="#pr4">地域分布</a></li>
          <li id="r5" @click="onePageNav('5')" :class="{'current':liselected=== '5'}"><a href="#pr5">词云统计</a></li>
          <li id="r6" @click="onePageNav('6')" :class="{'current':liselected=== '6'}"><a href="#pr6">负面走势</a></li>
          <!--<li id="r7" @click="onePageNav('7')" :class="{'current':liselected=== '7'}"><a href="#pr7">高频词汇</a></li>-->
          <!--<li id="r8" @click="onePageNav('8')" :class="{'current':liselected=== '8'}"><a href="#pr8">情感分析</a></li>-->

        </ul>
        <!--分析完毕 start-->

        <div class="reportPreview">
          <div class="logo">
          </div>
          <div class="reportCon">
            <!--报告标题 start-->
            <div class="row-fluid" id="ui-accordion-0">
              <div class="reportTit">
                <div class="textShow">
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <h1 id="analysisTitle" contenteditable="false" class="contenteditable">
                          {{report_name}}
                        </h1>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <!--报告标题 end-->
            <div class="reportBox ui-sortable">
              <!--评论统计 start-->
              <div class="row-fluid" id="ui-accordion-1" name="r1">
                <div class="textShow">
                  <div class="tit" id="pr1">
                    <div class="text">
                      <h2 id="contentTitle1" contenteditable="false" class="contenteditable modification">评论统计</h2>
                    </div>
                  </div>

                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">

                        <div contenteditable="false" class="textCon contenteditable" id="introduce">
                          <div class="y2 y2_1 float_l" style="width: 100%;">
                            <ul v-for="item in comment_data">
                              <li>
                                <p>{{item.author.name}}</p>
                                <p></p>
                                <div class="tx"><img
                                  :src=item.author.avatar_url>
                                </div>
                                <p></p>
                                  <p>描述：{{item.excerpt|filterString(40)}}</p>
                                <p>评论数：{{item.comment_count}}</p></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--评论统计 end-->
              <!--点赞统计 start-->
              <div class="row-fluid" id="ui-accordion-2" name="r2">
                <div class="textShow">
                  <div class="tit" id="pr2">
                    <div class="text">
                      <h2 id="contentTitle2" contenteditable="false" class="contenteditable modification">点赞统计</h2>
                    </div>
                  </div>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">

                        <div contenteditable="false" class="textCon contenteditable" id="vote">
                          <div class="y2 y2_1 float_l" style="width: 100%;">
                            <ul v-for="item in vote_data">
                              <li>
                                <p>{{item.author.name}}</p>
                                <p></p>
                                <div class="tx"><img
                                  :src=item.author.avatar_url>
                                </div>
                                <p></p>
                                <p>描述：{{item.excerpt|filterString(40)}}</p>
                                <p>点赞数：{{item.voteup_count}}</p></li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--点赞统计 end-->
              <!--男女比例 start-->
              <div class="row-fluid" id="ui-accordion-3" name="r3">
                <div class="textShow">
                  <div class="tit" id="pr3">
                    <div class="text">
                      <h2 id="contentTitle3" contenteditable="false" class="contenteditable modification">男女比例</h2>
                    </div>
                  </div>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <div class="mwbcom" id="echart1" style="height: 346px;width: 500px;float: left;">

                        </div>
                        <div class="mwbcom" id="echart2" style="height: 346px;width: 500px;float: right">

                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--男女比例 end-->
              <!--地域分布 start-->
              <div class="row-fluid" id="ui-accordion-4" name="r4">
                <div class="textShow">
                  <div class="tit" id="pr4">
                    <div class="text">
                      <h2 id="contentTitle4" contenteditable="false" class="contenteditable modification">地域分布</h2>
                    </div>
                  </div>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <div class="mwbcom" id="echart3" style="height: 346px;width: 500px;float: left">
                        </div>
                        <div class="info-section" style="width: 342px;float: right">
                          <div class="scrolling_outer" style="position: relative;">
                            <div id="scrollTabwrapper" class="scrolling_inner"
                                 style="border: 1px solid rgb(204, 204, 204); overflow: hidden auto; padding-right: 0px; height: 400px; width: 100%;">
                              <table border="0" cellspacing="" cellpadding=""
                                     class="map_table map_table2 _scrolling _thead"
                                     style="width: auto; display: block; position: absolute; border-top: none; border-right: none; border-bottom: 1px solid rgb(204, 204, 204); border-left: none; border-image: initial; top: 1px;background: #d0d5d4;">
                                <thead>
                                <tr>
                                  <th width="33%" style="width: 104px;">地域</th>
                                  <th width="" style="width: 211px;">人数</th>
                                </tr>
                                </thead>

                              </table>
                              <table id="scrollTab" border="0" cellspacing="" cellpadding=""
                                     class="map_table map_table2 _scrolling" style="width: 100%;">
                                <thead>
                                <tr>
                                  <th width="33%">地域</th>
                                  <th width="">人数</th>
                                </tr>
                                </thead>
                                <tbody id="c5_tb" class="ui-sortable">
                                <tr v-for="item in location_data">
                                  <td>&nbsp;{{item.name}}</td>
                                  <td>&nbsp;{{item.value}}</td>
                                </tr>
                                </tbody>
                              </table>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--地域分布 end-->
              <!--词云统计 start-->
              <div class="row-fluid" id="ui-accordion-5" name="r5">
                <div class="textShow">
                  <div class="tit" id="pr5">
                    <div class="text">
                      <h2 id="contentTitle5" contenteditable="false" class="contenteditable modification">词云统计</h2>
                    </div>
                  </div>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <div class="mwbcom" id="echart4" style="height: 436px;width: 800px;">
                        </div>

                      </div>
                    </li>
                  </ul>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <div class="mwbcom" id="echart5" style="height: 346px;width: 500px;float: left;">

                        </div>
                        <div class="mwbcom" id="echart6" style="height: 346px;width: 500px;float: right">

                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--词云统计 end-->
              <!--负面走势 start -->
              <div class="row-fluid" id="ui-accordion-6" name="r6">
                <div class="textShow">
                  <div class="tit" id="pr6">
                    <div class="text">
                      <h2 id="contentTitle6" contenteditable="false" class="contenteditable modification">负面走势</h2>
                    </div>
                  </div>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">
                        <div class="mwbcom" id="echart7" style="height: 436px;width: 800px;margin-left: 125px;">
                        </div>

                      </div>
                    </li>
                  </ul>
                  <ul class="column ui-sortable">
                    <li>
                      <div class="text tool tools">

                          <el-table :data="event_data">
                          <el-table-column
                            prop="title"
                            label="标题"
                            align="center"
                            width="430"
                          >
                          </el-table-column>
                            <el-table-column
                            prop="comment_count"
                            label="评论数量"
                            align="center"
                            width="200"
                          >
                          </el-table-column>
                            <el-table-column
                            prop="voteup_count"
                            label="点赞数量"
                            align="center"
                            width="200"
                          >
                          </el-table-column>

                            <el-table-column
                            prop="created_time"
                            label="时间"
                            align="center"
                            width="200"
                          ><template slot-scope="scope">
                        <!--{{scope.row.keyword}}-->
                        {{scope.row.created_time|filterDate}}
                      </template>
                          </el-table-column>
                        </el-table>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
              <!--负面走势 end-->
            </div>
          </div>
        </div>
      </div>
    </el-main>
  </el-container>
</template>
<!--<remote-script src="../../js/china.js"></remote-script>-->
<script>
  import * as echarts from 'echarts'
  import '../../../node_modules/echarts/map/js/china.js'
  import '../../../node_modules/echarts-wordcloud/dist/echarts-wordcloud.min.js'

  export default {
    name: "dataReport",
    data() {
      return {
        zhihu: {
          "zhihu_icu": "996icu",
          "zhihu_paris": "巴黎圣母院",
          "zhihu_car": "奔驰"
        },
        report_name: "网络传播分析报告",
        event_data: [],
        gender_data: {},
        location_data: [],
        vote_data: [],
        word_data: {},
        comment_data: [],
        option1: {
          title: {
            text: '男女比例饼图',
            // subtext: '纯属虚构',
            x: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
          },
          legend: {
            top: "30px",
            orient: 'horizontal',
            left: 'cenetr',
            data: ['女性', '男性', '其他']
          },
          series: [
            {
              name: '男女比例',
              type: 'pie',
              radius: ['40%', '70%'],
              // avoidLabelOverlap: false,

              data: [
                {value: 21335, name: '直接访问'},
                {value: 3150, name: '邮件营销'},
                {value: 210, name: '联盟广告'},

              ],
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        },
        option2: {
          title: {
            text: "男女比例柱状图",
            x: "center"
          },
          color: ['#3398DB'],
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              data: ['女性', '男性', '其他'],
              axisTick: {
                alignWithLabel: true
              }
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              name: '男女比例',
              type: 'bar',
              barWidth: '60%',
              data: [10, 52, 200]
            }
          ]
        },
        // 中国地图
        option3: {
          title: {
            text: '人员地域分布',
            // subtext: '纯属虚构',
            left: 'center'
          },
          tooltip: {
            trigger: 'item'
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: ['数量']
          },
          visualMap: {
            min: 0,
            max: 2500,
            left: 'left',
            top: 'bottom',
            text: ['高', '低'],           // 文本，默认为数值文本
            calculable: true
          },
          toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
              mark: {show: true},
              dataView: {show: true, readOnly: false},
              restore: {show: true},
              saveAsImage: {show: true}
            }
          },
          series: [
            {
              name: '数量',
              type: 'map',
              mapType: 'china',
              roam: false,
              label: {
                normal: {
                  show: true
                },
                emphasis: {
                  show: true
                }
              },
              data: [
                {name: '北京', value: Math.round(Math.random() * 1000)},
                {name: '天津', value: Math.round(Math.random() * 1000)},
                {name: '上海', value: Math.round(Math.random() * 1000)},
                {name: '重庆', value: Math.round(Math.random() * 1000)},
                {name: '河北', value: Math.round(Math.random() * 1000)},
                {name: '河南', value: Math.round(Math.random() * 1000)},
                {name: '云南', value: Math.round(Math.random() * 1000)},
                {name: '辽宁', value: Math.round(Math.random() * 1000)},
                {name: '黑龙江', value: Math.round(Math.random() * 1000)},
                {name: '湖南', value: Math.round(Math.random() * 1000)},
                {name: '安徽', value: Math.round(Math.random() * 1000)},
                {name: '山东', value: Math.round(Math.random() * 1000)},
                {name: '新疆', value: Math.round(Math.random() * 1000)},
                {name: '江苏', value: Math.round(Math.random() * 1000)},
                {name: '浙江', value: Math.round(Math.random() * 1000)},
                {name: '江西', value: Math.round(Math.random() * 1000)},
                {name: '湖北', value: Math.round(Math.random() * 1000)},
                {name: '广西', value: Math.round(Math.random() * 1000)},
                {name: '甘肃', value: Math.round(Math.random() * 1000)},
                {name: '山西', value: Math.round(Math.random() * 1000)},
                {name: '内蒙古', value: Math.round(Math.random() * 1000)},
                {name: '陕西', value: Math.round(Math.random() * 1000)},
                {name: '吉林', value: Math.round(Math.random() * 1000)},
                {name: '福建', value: Math.round(Math.random() * 1000)},
                {name: '贵州', value: Math.round(Math.random() * 1000)},
                {name: '广东', value: Math.round(Math.random() * 1000)},
                {name: '青海', value: Math.round(Math.random() * 1000)},
                {name: '西藏', value: Math.round(Math.random() * 1000)},
                {name: '四川', value: Math.round(Math.random() * 1000)},
                {name: '宁夏', value: Math.round(Math.random() * 1000)},
                {name: '海南', value: Math.round(Math.random() * 1000)},
                {name: '台湾', value: Math.round(Math.random() * 1000)},
                {name: '香港', value: Math.round(Math.random() * 1000)},
                {name: '澳门', value: Math.round(Math.random() * 1000)}
              ]
            }


          ]
        },
        //词云
        option4: {
          title: {
            text: '词云展示',
            x: 'center',
            marginTop: 100
          },
          toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
              mark: {show: true},
              dataView: {show: true, readOnly: false},
              magicType: {
                show: true,
                type: ['pie', 'funnel']
              },
              restore: {show: true},
              saveAsImage: {show: true}
            }
          },
          tooltip: {},
          series: [{
            type: 'wordCloud',  //类型为字符云
            shape: 'smooth',  //平滑
            gridSize: 2, //网格尺寸
            // size: ['80%', '80%'],
            sizeRange: [20, 100],
            rotationRange: [30, 80], //旋转范围
            //maskImage: maskImage,  //自定义图案
            textStyle: {
              normal: {
                fontFamily: 'sans-serif',
                color: function () {
                  return 'rgb('
                    + [Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160)]
                      .join(',') + ')';
                }
              },
              emphasis: {
                shadowBlur: 5,  //阴影距离
                shadowColor: '#333'  //阴影颜色
              }
            },
            data: [],
          }]
        },
        // 词云柱状图
        option5: {
          title: {
            text: '词频统计',
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          legend: {
            data: ['出现次数'],
            show: false
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
          },
          yAxis: {
            type: 'category',
            data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
          },
          series: [
            {
              name: '出现次数',
              type: 'bar',
              data: [18203, 23489, 29034, 104970, 131744, 630230]
            }
          ]
        },
        //词云的pie图
        option6: {
          title: {
            text: '词频的极坐标图'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
            }
          },
          angleAxis: {
            type: 'category',
            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
            z: 10
          },
          radiusAxis: {},
          polar: {},
          series: [{
            type: 'bar',
            data: [1, 2, 3, 4, 3, 5, 1],
            coordinateSystem: 'polar',
            name: '出现次数',
            stack: 'a'
          }],
          legend: {
            show: false,
            data: ['出现次数']
          }
        },
        // 负面走势
        option7: {
          title: {
            text: '负面走势',
            // subtext: '纯属虚构',
            x: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} {b} : {c} ({d}%)"
          },
           toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true,
                type: ['pie', 'funnel']
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
          // legend: {
          //   type: 'scroll',
          //   // orient: 'horizent',
          //   right: 10,
          //   top: 20,
          //   bottom: 20,
          //    // top: "30px",
          //   orient: 'horizontal',
          //   left: 'center',
          //   data: [1,2,3,4,5],
          //   show:true
          //   // selected: data.selected
          // },
          series: [
            {
              name: '走势热度',
              type: 'pie',
              radius: '55%',
              center: ['40%', '50%'],
              data:[],
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        },
        // 当前选择的tab栏
        liselected:"1"
      }
    },
    mounted() {

    },
    created() {
      this.GetReport();
    },
    methods: {
      // 切换class
      onePageNav(num){
         this.liselected = num;
      },
      // 设置echart面板数据
      drawOption(type) {
        let mychart = this.$echarts.init(document.getElementById('echart' + type));
        mychart.setOption(this["option" + type]);
      },
      //获取基本信息
      GetReport() {
        let data = {
          "data_name": this.$route.params.data_name,
          "keywords": this.zhihu[this.$route.params.data_name],
          "csrfmiddlewaretoken": this.getCookie('csrftoken')
        };
        this.$http({
          url: this.$store.state.location + "/api_report/",
          method: "POST",
          data: this.$Qs.stringify(data),
        }).then(response => {
          let result = response.data;
          this.report_name = result["data"].report_name;
          this.comment_data = result["data"].comment_data;
          this.vote_data = result["data"].vote_data;
          this.gender_data = result["data"].gender_data;
          this.option1.series[0].data = [
            {value: this.gender_data.female, name: '女性比例'},
            {value: this.gender_data.male, name: '男性比例'},
            {value: this.gender_data.unknowmale, name: '其他比例'},
          ];
          this.drawOption(1);
          this.option2.series[0].data = [this.gender_data.female, this.gender_data.male, this.gender_data.unknowmale]
          this.drawOption(2);
          // 地图
          this.location_data = result["data"].location_data;
          this.option3.series[0].data = this.location_data;
          // console.log(this.option3.series[0].data)
          this.drawOption(3);
          // 词云
          this.word_data = result["data"].word_data;
          this.option4.series[0].data = this.word_data;
          //console.log(this.option4.series[0].data);
          // let maskImage = new Image();
          // maskImage.src = '../../assets/e.jpg';
          // this.option4.series[0].maskImage = maskImage;
          this.drawOption(4);
          let categories = [];
          let x_data = [];
          for (var item in this.word_data) {
            if (item < 20) {
              categories.push(this.word_data[item].name);
              x_data.push(this.word_data[item].value);
            }
            else {
              break;
            }
          }
          this.option5.yAxis.data = categories;
          this.option5.series[0].data = x_data;
          this.drawOption(5);
          this.option6.angleAxis.data = categories;
          this.option6.series[0].data = x_data;
          this.drawOption(6);
          this.event_data = result['data'].event_data;
          let legend_data = [];
          let series_data = [];
          for (var i in this.event_data) {
            legend_data.push(this.event_data[i].title);
            series_data.push({"name":this.event_data[i].title,"value":parseInt(this.event_data[i].comment_count) + parseInt(this.event_data[i].voteup_count)})
          }
          // this.option7.legend.data = legend_data;
          // console.log(this.option7.legend.data);
          this.option7.series[0].data = series_data;
          this.drawOption(7);
        }).catch(error => {
          console.log(error);
        })
      }
    },
  }
</script>

<style scoped>
  .y2.y2_1 ul:first-child {
    border-bottom: solid 1px #6fc1bf;
  }

  .yxl_top .y2 {
    text-align: center;
    margin: 10px 0;
    width: 100%;
  }

  .y2 ul > li {
    margin: 0;
    width: 19%;
    padding-top: 5px;
    height: 240px;
    background-color: #fff;
    float: left;
    border: solid 3px #cee7d2;
    margin-bottom: 5px;
    margin-left: 4px;
  }

  .reportCon {
    background-color: #FAF9F9;
  }

  .reportCon .reportBox {
    padding: 20px 30px;
  }

  li {
    display: list-item;
    text-align: -webkit-match-parent;
  }

  .reportCon .reportBox .textShow > .text .textCon, .reportCon .reportBox .textShow .ui-sortable .text .textCon {
    min-height: 50px;
  }

  .reportCon .reportBox .tit {
    border-bottom: solid 1px #c4c4c4;
    height: 55px;
    line-height: 40px;
    color: #333;
    margin-bottom: 10px;
    text-align: left;
  }

  .reportCon .row-fluid .tit {
    border-bottom: solid 1px #c4c4c4;
    height: 55px;
    line-height: 40px;
    color: #333;
    margin-bottom: 10px;
    text-align: left;
  }

  .reportCon .reportBox .textShow .text, .textCon .text2, .reportCon .reportBox .textShow .column .text, .reportCon .row-fluid .textShow .text {
    font-size: 14px;
    line-height: 25px;
    color: #666;
    margin-bottom: 10px !important;
    display: inline-block;
    clear: both;
  }

  .row-fluid .textShow ul {
    margin: 0px;
    padding: 0px;
    list-style-type: none;
  }

  .yb2 h2 {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    line-height: 80px;
    background-color: #ff8400;
    font-size: 12px;
    color: #fff;
    text-align: center;
    margin-left: 10px;
  }

  .yb2 .more a {
    border: solid 1px #e7e7e7;
  }

  .packUp2 a {
    margin-top: -1px;
  }

  .packUp a, .packUp2 a {
    display: block;
    width: 120px;
    height: 22px;
    line-height: 22px;
    text-align: center;
    background-color: #fff;
    color: #737373;
    text-decoration: none;
    margin: 0px auto;
    border: solid 1px #e7e7e7;
    border-top: solid 1px #fff;
    font-size: 12px;
    margin-top: -1px;
  }

  .float_l {
    float: left;
  }

  .yb2 .line {
    display: block;
    width: 2px;
    height: 100%;
    background: #ff8400;
    position: absolute;
    z-index: 1;
    top: 0px;
    left: 50px;
  }

  .yb2 .round {
    display: block;
    width: 15px;
    height: 15px;
    line-height: 15px;
    text-align: center;
    -moz-border-radius: 22px;
    -webkit-border-radius: 22px;
    border-radius: 22px;
    border: solid 1px #ff8400;
    background-color: #ff8400;
    position: absolute;
    z-index: 2;
    top: 42px;
    left: 43px;
  }

  .contenteditable {
    padding: 0 10px;
  }

  .packUp, .packUp2 {
    border-top: solid 1px #e7e7e7;
    margin-top: 0px;
    margin-bottom: 8px;
  }

  .yb2 .more {
    position: absolute;
    bottom: 30px;
    right: 55px;
  }

  /* CSS Document */
  input, textarea {
    font-family: "微软雅黑";
  }

  .row-fluid {
    display: inline-block;
    width: 100%;
  }

  .reportWeb {
    width: 1200px;
    margin: auto;
  }

  .float_l {
    float: left;
  }

  .yb2 .roundEnd {
    display: block;
    width: 32px;
    height: 32px;
    line-height: 32px;
    text-align: center;
    -moz-border-radius: 32px;
    -webkit-border-radius: 32px;
    border-radius: 32px;
    border: solid 1px #ff8400;
    background-color: #ff8400;
    color: #fff;
    position: absolute;
    z-index: 2;
    bottom: -22px;
    left: 34px;
  }

  .yb2 .text:after {
    content: "";
    position: absolute;
    top: 28px;
    left: -10px;
    border-bottom: 10px solid transparent;
    border-top: 10px solid transparent;
    border-right: 10px solid #EDEDED;
  }

  /*报告左侧浮动导航*/
  #nav2 {
    list-style: none;
    position: fixed;
    min-width: 100px;
    top: 30px;
    z-index: 0;
  }

  #nav2 li {
    margin-bottom: 2px;
  }

  #nav2 a {
    background: #fff;
    color: #666;
    display: block;
    font-size: 14px;
    padding: 8px 10px;
    text-decoration: none;
    text-transform: uppercase;
    border-radius: 5px 0px 0px 5px;
    margin-left: 35px;
    border-bottom: 2px solid #dddddd !important;
    transition: margin-left 0.5s, background-color 0.5s, border-bottom 0.5s, color 0.5s;
    -moz-transition: margin-left 0.5s, background-color 0.5s, border-bottom 0.5s, color 0.5s;
    -webkit-transition: margin-left 0.5s, background-color 0.5s, border-bottom 0.5s, color 0.5s;
    -o-transition: margin-left 0.5s, background-color 0.5s, border-bottom 0.5s, color 0.5s;
  }

  #nav2 a:hover {
    background-color: #ff8500 !important;
    color: #fff !important;
    font-weight: 600;
    border-bottom: solid 2px #DF7400 !important;
    margin-left: 5px;
  }

  #nav2 .current a {
    background: #FF8500;
    color: #fff;
    margin-left: 5px;
  }

  /*分析报告预览*/
  .reportPreview .tool {
    top: 0px;
    right: 5px;
  }

  .reportPreview {
    width: 1100px;
    margin: 20px 0;
    margin-left: 150px;
    margin-right: 20px;
    background-color: #fff;
    position: relative;
    font-size: 12px;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-box-shadow: 0 0 4px 1px rgba(0, 0, 0, 0.5);
    -webkit-box-shadow: 0 0 4px 1px rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 4px 1px rgba(153, 153, 153, 0.5);
    overflow: hidden;
  }

  .row-fluid > .textShow .chart, .row-fluid > .textShow .chart img {
    display: inline-block;
    width: 100%;
  }

  .reportPreview .row-fluid {
    overflow: initial;
    display: inline-block;
    width: 100%;
  }

  .reportPreview .tool.toolhover {
    display: none;
  }

  .reportPreview .tool .button4 {
    height: 30px;
    line-height: 30px;
    background-color: transparent;
    color: #008be3;
    font-weight: 600;
    border: none;
  }

  .reportPreview .tool .button4:hover {
    background-color: #d7efff;
  }

  .logo {
    position: absolute;
    left: 40px;
    top: 20px;
    z-index: 2;
  }

  .reportCon {
    background-color: #FAF9F9;
  }

  .reportCon .reportTit {
    padding: 0px;
    min-height: 90px;
    text-align: center;
    border-bottom: solid 1px #dadada;
    background-color: #fff;
    position: relative;
  }

  .reportCon .reportTit .textShow {
    padding: 20px 0;
  }

  .reportCon .reportTit > i {
    position: absolute;
    bottom: -25px;
    left: 48.3333%;
    font-style: normal;
    color: #F00;
    font-size: 40px;
    text-shadow: 6px 0 6px #fff, 0 6px 6px #fff, 0 -6px 6px #fff, -6px 0 6px #fff;
  }

  .reportCon .reportTit .text, .reportBox .text {
    position: relative;
    margin-bottom: 0 !important;
  }

  .text .delete, .text .yb-delete, .text .yb-add, .text .yb-move {
    position: absolute;
    color: #008be3;
    font-size: 18px;
    display: inline-block;
    width: 25px;
    height: 25px;
    line-height: 25px;
    text-align: center;
    top: 30px;
    right: -28px;
    cursor: pointer;
    z-index: 1;
  }

  .text .yb-move {
    right: inherit;
    right: -28px;
    top: 2px;
    cursor: move;
  }

  .text .yb-add {
    top: 57px;
  }

  .reportCon .reportTit h1, .reportCon .reportTit .text {
    display: inline-block;
    padding: 5px 0px;
    font-size: 30px;
    width: 60%;
    color: #000;
    margin-bottom: 0px;
    margin-right: 10px;
  }

  .reportCon .reportTit .h1, .reportCon .reportTit .h2 {
    text-align: center; /*background-color:#F3F3F3;*/
  }

  .reportCon .reportTit .text {
    padding: 0;
  }

  .text .textCon {
    min-height: 45px;
  }

  .reportCon .reportTit .text h1 {
    width: 99.8%;
  }

  .reportCon .reportTit .text .textCon {
    font-size: 16px;
    padding: 5px 0;
    color: #888;
    font-weight: 300;
  }

  .reportCon .reportTit .rtime {
    color: #5f5f5f;
    font-size: 18px;
  }

  .reportCon .reportBox {
    padding: 20px 30px;
  }

  .reportCon .reportBox .tit h2 {
    display: inline-block;
    margin-right: 10px;
    float: left;
    font-size: 20px;
    line-height: 38px;
    border-bottom: solid 3px #008be3;
    color: #333;
    padding: 0px 5px;
    font-weight: bold;
    text-align: left;
  }

  .reportCon .reportBox .tit h2[contenteditable="true"] {
    min-width: 200px;
    max-width: 700px;
    overflow: hidden;
  }

  .reportCon .reportBox .tit span.small {
    line-height: 45px;
    font-size: 14px;
  }

  .reportCon .reportBox .textShow .column {
    min-height: 40px;
  }

  .reportCon .reportBox .textShow .text, .textCon .text2, .reportCon .reportBox .textShow .column .text {
    font-size: 14px;
    line-height: 25px;
    color: #666;
    margin-bottom: 10px !important;
    display: inline-block;
    clear: both;
  }

  .reportCon .reportBox .textShow > .text, .reportCon .reportBox .textShow .column .text {
    width: 100%;
    margin: 10px 0 !important;
  }

  .reportCon .reportBox .textShow .column .yb2 ul li {
    width: 100%;
  }

  .yb2 ul li {
    padding-left: 5px;
    line-height: 50px;
    color: #2b2b2b;
    font-size: 13px;
    float: left;
    clear: both;
    position: relative;
    padding-bottom: 10px;
  }

  .reportCon .reportBox .textShow .column .yb2 .text {
    width: 85%;
    line-height: 20px;
    padding: 5px;
    margin-left: 60px !important;
    margin-top: 13px !important;
    min-height: 60px;
    background: #ebe9e9;
    border-radius: 5px;
    text-align: left;
  }

  .reportCon .reportBox .textShow > .text .textCon, .reportCon .reportBox .textShow .ui-sortable .text .textCon {
    min-height: 50px;
  }

  .textCon .text2 {
    text-indent: 10px;
  }

  .reportCon .reportBox p {
    font-size: 14px;
  }

  .reportCon .reportBox p a {
    color: #444;
  }

  .reportCon .reportBox p em {
    font-weight: bold;
    color: #000;
    font-style: normal;
  }

  .reportCon .reportBox .img {
    border: solid 1px #CCC;
  }

  .reportCon .table {
    width: 100%;
    border: solid 1px #e7e7e7;
    margin: 0px;
    background-color: #fff;
  }

  .reportCon .table td {
    padding: 10px;
  }

  .reportCon .table th {
    background-color: #EEEEEE;
  }

  .reportCon .table .tdCon {
    text-align: left;
    padding: 10px;
  }

  .reportCon .table .tdCon p {
    text-indent: 25px;
    margin-bottom: 5px;
    line-height: 22px;
    padding: 0px;
  }

  .reportCon2 .line1 {
    border-bottom: solid 2px #0891ff;
    margin-bottom: 4px;
    margin-top: 20px;
  }

  .reportCon2 .line2 {
    border-bottom: solid 4px #0891ff;
  }

  .reportCon2 .reportTit h1 {
    color: #0891ff;
  }

  .reportCon2 .reportTit {
    margin: 0px 70px;
    background-color: transparent;
    border-bottom: none;
  }

  .reportCon2 .reportBox .tit {
    border-bottom: none;
  }

  .reportCon2 .reportBox .tit h2 {
    border-bottom: none;
  }

  .bottom {
    padding: 10px 0;
  }

  /*统计图选择*/
  .chartChoice {
    display: inline-block;
    width: 90%;
    margin: 20px 0;
    margin-left: 5%;
  }

  .chartChoice > ul > li {
    display: inline-block;
    width: 30.6%;
    margin-right: 2%;
    margin-bottom: 5px;
    border: solid 2px #dadada;
    cursor: pointer;
    position: relative;
  }

  .chartChoice > ul > li:hover, .chartChoice > ul > li.clicked {
    border: solid 2px #FF8500;
  }

  .chartChoice > ul > li:last-child {
    margin-right: 0%;
  }

  .chartChoice > ul > li.clicked p:last-child {
    background-color: #FF8500;
    color: #fff;
  }

  .chartChoice > ul > li.clicked:after {
    content: "√";
    width: 30px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    background-color: #FF8500;
    color: #fff;
    position: absolute;
    top: 0px;
    right: 0px;
  }

  .chartChoice > ul > li p:first-child {
    width: 100%;
    height: 140px;
  }

  .chartChoice > ul > li p:first-child img {
    width: 100%;
  }

  .chartChoice > ul > li p:last-child {
    width: 100%;
    font-size: 16px;
    text-align: center;
    line-height: 50px;
    border-top: solid 1px #dadada;
  }

  .chartMap img {
    width: 100%;
  }

  .text.tool {
    position: relative;
    overflow: hidden;
    z-index: 1;
    border: solid 1px;
    border-color: transparent;
  }

  .text.tool:hover {
    border: solid 1px #008BE3;
  }

  .chartMapBK {
    margin-bottom: 10px;
    position: relative;
    z-index: 1;
  }

  .chartMapBK:hover .control, .text.tool:hover .control {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }

  .control {
    position: absolute;
    z-index: 2;
    top: 0;
    right: 0;
    width: 52px;
    height: 100%;
    background-color: #f5f5f5;
    border-left: 1px solid #e0e0e0;
    -webkit-transform: translateX(60px);
    transform: translateX(60px);
    -webkit-transition: -webkit-transform .2s;
    transition: transform .2s;
    list-style-type: none;
  }

  .control li b {
    display: block;
    height: 46px;
    width: 52px;
    line-height: 46px;
    text-align: center;
    cursor: pointer;
    font-size: 18px;
  }

  .control li b:hover {
    background-color: #5faee3;
    color: #fff;
  }

  .tools .control {
    width: auto;
    height: 25px;
    border-top: 1px solid #e0e0e0;
    top: initial;
    bottom: 0;
    -webkit-transform: translateY(50px);
    transform: translateY(50px);
  }

  .tools .control li {
    float: left;
    display: block;
  }

  .tools .control li b {
    width: 25px;
    height: 25px;
    line-height: 25px;
    font-size: 15px;
  }

  .textShow {
    display: inline-block;
    width: 100%;
    word-break: break-all;
  }

  .row-fluid.hover .textShow, .row-fluid.hover .yb .toolhover {
    display: none;
  }

  .row-fluid.hover .editBox {
    display: inline-block;
  }

  .row-fluid.hover .tit h2 {
    border-bottom: solid 3px #FF8500;
    display: inline-block;

    margin-right: 10px;
  }

  .row-fluid.hover .tit input {
    padding: 5px 10px;
    margin-right: 10px;
    font-size: 20px;
    line-height: 26px;
    display: inline-block;
  }

  /*编辑样式*/
  .editBox {
    width: 100%;
    display: none;
    font-size: 14px;
    position: initial;
  }

  .yb > .editBox {
    position: absolute;
  }

  .reportTit .editBox > div {
    height: 100%;
    margin: 0px;
    padding: 20px 0;
  }

  .reportTit .editBox {
    min-height: initial;
  }

  .editBox > div {
  }

  .editBox .inputList {
    width: 98%;
    height: 100px;
    padding: 10px;
    line-height: 20px;

    margin-bottom: 10px;
    overflow-y: hidden;
  }

  .editBox .tool {
    display: inline-block;
  }

  .reportTit .tool {
    margin-top: 10px;
  }

  .reportTit .editBox .tool {
    display: inline-block;
  }

  .editBox input {
    background-color: #fff;
    border: solid 1px #dadada;
    border-radius: 2px;
  }

  .row-fluid:hover .tool {
    display: inline-block;
  }

  .editBox .table input {
    padding: 5px 10px;
  }

  .editBox .table .tool > button {
    padding: 0 5px;
  }

  .editBox .table .tool > button > i {
    margin-top: 0px;
    margin-right: 0px;
  }

  /*媒体来源占比*/
  .circularChart {
    width: 100%;
    height: 410px;
    position: relative;
  }

  .circularChart li {
    display: inline-block;
    position: absolute;
    background-color: rgba(34, 123, 192, .95);
    color: #fff;
    text-align: center;
    border-radius: 50%;
    width: 80px;
    height: 80px;
  }

  .circularChart li p {
    font-size: 13px;
    line-height: 18px;
  }

  .circularChart li p:first-child {
    margin-top: 20%;
  }

  .circularChart li.c1 {
    width: 200px;
    height: 200px;
    top: 121px;
    left: 143px;
  }

  .circularChart li.c1 p {
    font-size: 20px;
    line-height: 35px;
  }

  .circularChart li.c1 p:first-child {
    margin-top: 30%;
  }

  .circularChart li.c2 {
    width: 90px;
    height: 90px;
    top: 110px;
    left: 57px;
    background-color: rgba(34, 123, 192, .95);
  }

  .circularChart li.c3 {
    width: 85px;
    height: 85px;
    top: 46px;
    left: 128px;
    background-color: rgba(34, 123, 192, .90);
  }

  .circularChart li.c4 {
    width: 85px;
    height: 85px;
    top: 31px;
    left: 222px;
    background-color: rgba(34, 123, 192, .85);
  }

  .circularChart li.c5 {
    width: 85px;
    height: 85px;
    top: 73px;
    left: 306px;
    background-color: rgba(34, 123, 192, .80);
  }

  .circularChart li.c6 {
    width: 80px;
    height: 80px;
    top: 155px;
    left: 348px;
    background-color: rgba(34, 123, 192, .75);
  }

  .circularChart li.c7 {
    width: 70px;
    height: 70px;
    top: 239px;
    left: 339px;
    background-color: rgba(34, 123, 192, .70);
  }

  .circularChart li.c8 {
    width: 70px;
    height: 70px;
    top: 299px;
    left: 293px;
    background-color: rgba(34, 123, 192, .65);
  }

  .circularChart li.c9 {
    width: 60px;
    height: 60px;
    top: 326px;
    left: 231px;
    background-color: rgba(34, 123, 192, .60);
  }

  .circularChart li.c10 {
    width: 60px;
    height: 60px;
    top: 319px;
    left: 163px;
    background-color: rgba(34, 123, 192, .55);
  }

  .circularChart li.c11 {
    width: 55px;
    height: 55px;
    top: 285px;
    left: 113px;
    background-color: rgba(34, 123, 192, .50);
  }

  .circularChart li.c12 {
    width: 50px;
    height: 50px;
    top: 236px;
    left: 85px;
    background-color: rgba(34, 123, 192, .50);
  }

  .circularChart li.c11 p, .circularChart li.c12 p {
    line-height: 12px;
    font-size: 12px;
  }

  .circularChart li.c9 p, .circularChart li.c10 p {
    line-height: 16px;
    font-size: 12px;
  }

  .circularChart li.c7 p:first-child, .circularChart li.c8 p:first-child, .circularChart li.c9 p:first-child, .circularChart li.c10 p:first-child {
    margin-top: 12%;
  }

  .yb2 .more {
    position: absolute;
    bottom: 30px;
    right: 55px;
  }

  .yb2 .more a {
    border: solid 1px #e7e7e7;
  }

  .row-fluid.foot {
    display: none;
  }

  .mobileStyle #nav2 {
    top: 124px;
  }

  .dropdown-menu li .mwbBorder {
    display: none;
  }

  table i {
    display: inline-block;
    color: #008be3;
    width: 25px;
    height: 25px;
    text-align: center;
    line-height: 25px !important;
    font-size: 18px;
    cursor: pointer;
  }

  table i:hover {
    background-color: #d7efff;
  }

  @media only screen and (max-width: 1280px ) {
    #nav2 a {
      font-size: 12px;
    }
  }

  @media only screen and (max-width: 1024px ) {
    .reportPreview {
      width: 900px;
    }
  }

  @media only screen and (max-width: 750px ) {
    .row-fluid.foot {
      display: block;
    }

    .reportWeb {
      width: 100%;
      margin: auto;
    }

    .page-container {
      max-width: 100%;
    }

    #nav2 {
      display: none;
    }

    .reportPreview {
      width: 100%;
      margin: 0;
      -moz-border-radius: 0px;
      -webkit-border-radius: 0px;
      border-radius: 0px;
    }

    .reportPreview .row-fluid {
      box-shadow: 1px 0px 1px rgba(0, 0, 0, 0.4);
      background-color: #fff;
    }

    .row-fluid .row-fluid {
      box-shadow: none;
      margin: 0;
    }

    .reportCon .reportBox .tit h2 {
      font-size: 16px;
      padding: 0px 10px;
      border-bottom: none;
      font-weight: 300;
    }

    .reportCon .reportBox {
      padding: 0px;
    }

    .reportCon .reportBox .tit {
      border-bottom: solid 1px #DDDDDD;
      margin-bottom: 0;
      height: 38px
    }

    .logo {
      position: initial;
      left: initial;
      top: initial;
    }

    .reportCon .reportTit {
      height: auto;
    }

    .reportCon .reportTit .textShow {
      padding: 5px 0;
    }

    .reportCon .reportTit h1, .reportCon .reportTit .h1 {
      font-size: 18px;
      margin: 0;
    }

    .reportCon .reportBox .textShow > .text, .textCon .text2 {
      margin: 0px;
    }

    .reportCon .reportTit {
      min-height: 65px;
    }

    .textCon {
      margin: 10px;
    }

    .chart .textCon {
      margin: 0;
    }

    .yb2 {
      margin: 10px;
    }

    .yb2 h2 {
      width: 100px;
      height: 35px;
      line-height: 35px;
      text-align: center;
      margin-left: 0px;
      border-radius: 20px;
    }

    .yb2 .line {
      left: 20px;
    }

    .yb2 .round {
      left: 13px;
    }

    .yb2 .roundEnd {
      left: 5px;
    }

    .yb2 .text {
      margin-left: 39px;
    }

    .reportCon .reportBox .textShow .column .yb2 .text {
      margin-left: 40px !important;
      margin-top: -15px !important;
    }

    .yb2 .text2 {
      width: auto;
    }

    .yb2 .more {
      right: 5px;
    }

    .mwb5 {
      width: 100%;
    }

    .mwbBorder > .text {
      line-height: 20px;
    }

    .mwbBorder {
      border: none;
    }

    .mwbBorder .mwbcon .float_r {
      width: 100%;
    }

    .mwbcon {
      overflow: auto;
    }

    .mwblist ul > li {
      width: 50%;
    }

    .mwblist2 ul > li, .mwblist3 ul > li {
      width: 100%;
      padding: 0;
      border-radius: 0px;
      -moz-box-shadow: none;
      -webkit-box-shadow: none;
      box-shadow: none;
      border-bottom: dashed 1px #D8D8D8;
      margin: 0;
      padding: 10px 0;
    }

    /* .mwblist2 ul > li:last-child,.mwblist3 ul > li:last-child{border: none;}*/
    .mwblist ul > li .tx {
      margin: 0 10px;
      width: 40px;
      height: 40px;
    }

    .mwblist3 ul > li p.wbText {
      margin: 0 10px;
    }

    .genderBox, .biliBox {
      top: initial;
      left: initial;
      position: initial;
      clear: both;
      width: 90%;
      margin-left: 5%;
    }

    .gender, .bili {
      width: 50%;
      float: left;
      margin: 0;
    }

    .gender i {
      margin-left: 15px;
    }

    .genderBox .gender:first-child {
      margin-bottom: 30px;
    }

    .info-section {
      position: initial;
      top: initial;
      right: initial;
      width: 100%;
      float: left;
    }

    .biliBox3 {
      width: 98%;
      margin-left: 1%;
    }

    .biliBox3 .bili strong {
      font-size: 12px;
      line-height: 12px;
    }

    .biliBox3 .bili i {
      width: 10px;
      height: 10px;
      margin-right: 5px;
    }
  }
</style>
