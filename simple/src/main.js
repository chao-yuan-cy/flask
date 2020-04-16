// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// 引入 路由模块
import VueRouter from 'vue-router'

import Base from './Base.vue'
// 引入 单文件组件
import IndexPage from './components/index.vue'
import mock from './mock/mock'

Vue.config.productionTip = false
// 调用
Vue.use(VueRouter)
// 实例化一个router
let router = new VueRouter({
  // 回退键  查看历史记录  开启浏览器保存历史的功能
  // history 是一个字符串
  mode:'history',
  routes:[
    {
      // 根路径
      path:'/',
      // 指定哪个组件
      component:IndexPage
    }
  ]

})

new Vue({
  el: '#app',
  // 注册进router 
  router,
  components: { 
    Base
   },
  template: '<Base/>'
})
