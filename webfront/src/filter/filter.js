import Vue from 'vue'
/*
* 日期过滤器 时间戳转出通用日期格式
*
* */
Vue.filter('filterDate', function (value) {
  if (value === "undefind" || value == undefined || value == null || value === "" || value === "null" || value == -1 || value === 0) {
    return "--"
  }
  let date = new Date(parseInt(value));
  return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
})
/**
 * 字符串截取
 *
 */

Vue.filter('filterString', function (value, number) {
  if (value === "undefind" || value == undefined || value == null || value === "" || value === "null" || value == -1 || value === 0) {
    return "**"

  } else if (value.length <= number) {
    return value
  }
  return value.slice(0, number) + "...";
});
/**
 * 时间格式化
 */
Vue.filter("filterYmd", function (t) {
  if (t === '' || t === null) {
    return t
  }
  if (t === "--") {
    return t
  }
  if (parseInt(t) <= 0 || parseInt(t) === -1) {
    return '--'
  }
  if ((t.toString()).length > 13) {
    return "--"
  }
  // t = parseFloat(parseInt(t) / 1000.0);
  let date = new Date();
  let current_time = parseInt(date.getTime());
  if (t > current_time) {
    return "--"
  }
  else {
    var d = new Date(t);
    let Y = d.getFullYear() + "-";
    let M = (d.getMonth() + 1 < 10 ? '0' + (d.getMonth() + 1) : d.getMonth() + 1) + '-';
    let D = d.getDate() + ' ';
    return Y + M + D
  }
});
/*
* 日期过滤器 时间戳转出通用日期格式
*
* */
Vue.filter('filterDate', function (value) {
  if (value === "undefind" || value == undefined || value == null || value === "" || value === "null" || value == -1 || value === 0) {
    return "--"
  }
  let date = new Date(parseInt(value)*1000);
  return date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
});
/*
* 用户类型过滤
**/
Vue.filter('filterType',function (value) {
  if(value === 1){
    return "超级管理员"
  }
  else{
    return "普通用户"
  }
});
