// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import store from './vuex'
Vue.use(store);
//引入element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI);

//引入axios
import axios from 'axios'
Vue.prototype.$http = axios;

//引入echarts
import echarts from 'echarts'
Vue.use(echarts);
Vue.prototype.$echarts = echarts;

//引入qs
import Qs from 'qs'
Vue.use(Qs);
Vue.prototype.$Qs = Qs;

import { Loading,Message } from 'element-ui'
// Vue.use(store);
// Vue.prototype.$store = store;

import promise from 'es6-promise'
/* eslint-disable no-new */
Vue.config.productionTip = false;

//获取cookie
Vue.prototype.getCookie = function (name) {
  name = name + "=";
  var start = document.cookie.indexOf(name),
    value = null;
  //如果cookies存在
  if (start > -1){
    var end = document.cookie.indexOf(";",name);
    if(end == -1){
      end = document.cookie.length;
    }
    value = document.cookie.substring(start+name.length,end);
  }
  return value;
}
// 超时时间
axios.defaults.timeout = 600000;

//设置请求拦截
var loadinginstace;
Vue.prototype.$requestInterceptor = axios.interceptors.request.use(
    config => {
      loadinginstace = Loading.service({ fullscreen: true ,background:"rgba(0,0,0,0)"});

      // console.log(sessionStorage.hasOwnProperty("token") && sessionStorage.hasOwnProperty("now_user_id"))
      if(router.currentRoute.name !='login'){
        if(sessionStorage.hasOwnProperty("token") && sessionStorage.hasOwnProperty("now_user_id")) {
          //console.log(sessionStorage.getItem("token"));
          config.headers= {
            'Content-Type':'application/x-www-form-urlencoded',
            'Authorization':sessionStorage.getItem("token"),
            // csrfmiddlewaretoken:this.getCookie("csrftoken")
          };
        }else {

          console.log('sessionStorage没登录token');
          router.push({name:'login',query:{redirect: decodeURIComponent(router.currentRoute.fullPath)}})

        }
      }
                return config;
    },
    err => {
      Message.error({
        message: '加载超时'
      })
        return Promise.reject(err);
    });

// http响应拦截器
// axios.interceptors.response.forEach(function (e) {
//   console.log(e)
// })
Vue.prototype.$responseInterceptor = axios.interceptors.response.use(data => {
  // 响应成功关闭loading

  loadinginstace.close();
  return data
}, error => {
  loadinginstace.close();

  if (error.response) {
    switch (error.response.status) {
      case 401:
        // 这里写清除token的代码
        if(router.currentRoute.name !='login'){
          sessionStorage.removeItem("token");
          router.push({name:'login',query:{redirect: decodeURIComponent(router.currentRoute.fullPath)}})
        }
        break;
      default:
        Message.info({
          message: '加载失败'
        });

    }
  }
  return Promise.reject(error)
});

// router.beforeEach((to, from, next) => {
//   if (!to.meta.requireAuth) {  // 判断该路由是否需要登录权限
//     if (sessionStorage.hasOwnProperty("token")) {  // 通过vuex state获取当前的token是否存在
//       next();
//     }
//     else {
//       next({
//         path: '/login',
//         query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
//       })
//     }
//   }
//   else {
//     next();
//   }
// })
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
