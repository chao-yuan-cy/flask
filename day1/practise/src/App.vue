<template>
  <!-- <div id="app">
    <img src="./assets/logo.png" />
    <router-view />
  </div>-->
<div class="container">
  <h2>我的购物车清单</h2>
  <!-- 输入框 添加按钮 js-new-item 自定义的-->
  <div class="input-group">
    <input type="text" class="js-new-item form-control" placeholder="添加想要购买的商品" />
    <span class="input-group-btn">
      <button type="button" class="js-add btn btn-default">添加到购物车</button>
    </span>
  </div>

  <!-- 无序列表 -->
  <ul>
    <li>
      <div class="checkbox">
        <label for>
          <input type="checkbox" class="js-item" />苹果
        </label>
      </div>
    </li>
    <li>
      <div class="checkbox">
        <label for>
          <input type="checkbox" class="js-item" />手机
        </label>
      </div>
    </li>
    <li>
      <div class="checkbox">
        <label for>
          <input type="checkbox" class="js-item" />电脑
        </label>
      </div>
    </li>
  </ul>
  <!--改变标题 -->
  <div class="footer">
    <hr />
    <span>改变标题</span>
    <input type="text" value="我的购物车清单" class="js-change-titile" />
  </div>
</div>
</template>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

.container {
  width: 50%;
  margin: 100px auto;
}
.removed {
  color: grey;
}

.removed label {
  text-decoration: line-through;
}
ul {
  border: 1px solid black;
  margin-top: 30px;
}
ul li {
  list-style: none;
}
</style>
