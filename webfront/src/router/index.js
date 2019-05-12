import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import login from '@/components/login'
import HomePage from '@/components/common/HomePage'
import hotDaily from '@/components/common/hotDaily'
import newsWatch from '@/components/common/newsWatch'
import spiderManage from '@/components/common/spiderManage'
import userManage from '@/components/common/userManage'
import dataReport from '@/components/common/dataReport'
import dataAnalysis from '@/components/common/dataAnalysis'
Vue.use(Router);

export default new Router({
  mode: "history",//去掉#
  base:'/',
  routes: [
     {
      path: '', redirect: '/login'
    },
    {
      path:'/login',
      name:"login",
      component:login
    },
    {
      path:"/HomePage",
      name:"HomePage",
      component:HomePage,
      redirect:'/HomePage/hotDaily',
      children:[
        {
          path:'',
          redirect:'hotDaily'
        },
        {
          path:"/HomePage/hotDaily",
          name:'hotDaily',
          component:hotDaily
        },
        {
          path:"/HomePage/newsWatch",
          name:'newsWatch',
          component:newsWatch
        },
        {
          path:"/HomePage/spiderManage",
          name:'spiderManage',
          component:spiderManage
        },
        {
          path:"/HomePage/userManage",
          name:'userManage',
          component:userManage
        },
        {
          path:"/HomePage/dataAnalysis",
          name:'dataAnalysis',
          component:dataAnalysis
        }
      ]
    },
    {
       path:"/dataReport",
      name:'dataReport',
      component:dataReport
    }

  ]
})
