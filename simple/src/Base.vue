<template>
  <div id="app">
    <div class='app-head'>
      <div class='app-head-inner'>
        <img src="./assets/logo.png" alt=""><span class='app-title'>海马生鲜商城</span>
        <div class='head-nav'>
        <ul>
          <li>登录</li>
          <li class='nav-pile'>|</li>
          <li>注册</li>
          <li class='nav-pile'>|</li>
          <li>关于</li>
        </ul> 
      </div>
      </div>
      

    </div>
    <div class='app-content'>
      <router-view ></router-view>
    </div>
    <div class='app-foot'>
      <p>&copy;1901C-2020</p>
    </div>

  </div>
</template>

<script>
export default {

}
</script>

<style>
/* reset 样式 */
html,body,div,span,applet,object,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video {
	margin:0;
	padding:0;
	border:0;
	font-size:100%;
	font:inherit;
	font-weight:normal;
	vertical-align:baseline;
}
ol,ul,li {
	list-style:none;
}
blockquote,q {
	quotes:none;
}
blockquote:before,blockquote:after,q:before,q:after {
	content:'';
	content:none;
}
table {
	border-collapse:collapse;
	border-spacing:0;
}
th,td {
	vertical-align:middle;
}
/* custom */
a {
	outline:none;
	color:#16418a;
	text-decoration:none;
	-webkit-backface-visibility:hidden;
}
a:focus {
	outline:none;
}
input:focus,select:focus,textarea:focus {
	outline:-webkit-focus-ring-color auto 0;
}
/* base.Vue */
body{
  background: #f0f2f5;
  font-size: 14px;
  color: #444;
}
.app-head{
  width: 100%;
  height: 90px;
  line-height: 100px;
  color: #b2b2b2;
  background: #363636;
}
.app-head-inner{
  width: 1200px;
  margin: 0 auto;
}
.app-title{
  font-size:50px;
  margin-left: 30px;
}
.app-head-inner img{
  width: 50px;
  margin-top: 20px;
  float: left;
}
.head-nav{
  float: right;
}
.head-nav li{
  float: left;
  cursor: pointer;
}
.nav-pile{
  padding: 0 10px;
}
/* *{
  padding: 0;
  margin: 0;
} */
.app-content{
  width: 1200px;
  margin: 0 auto;
}
.app-foot{
  text-align: center;
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: #e3e4e8;
  margin-top: 30px;
}

</style>
