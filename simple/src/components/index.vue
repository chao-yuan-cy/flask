<template>
    <div class='index-wrapper'>
        <div class='index-left'>
            <div class="index-left-block all-products">
                <h2>全部产品</h2>
                <template v-for="product in productList">
                <h3>{{ product.title}}</h3>
                    <ul>
                        <li v-for='item in product.list'>
                            <a v-bind:href='item.url'>{{item.title}}</a>
                            <span v-if="!item.hot" class='hot-tag'>hot</span>
                        </li>
                    </ul>
                <hr v-if="!product.last"/>
                </template>
            </div>
            <div class="index-left-block lastest-news">
                <h2>最新消息</h2>
                <template v-for="m in mess_new">
                    <!-- <p>{{ m }}</p> -->
                    <ul>
                        <li v-for='item in m'>
                            <p>{{ item.title }}</p>
                        </li>
                    </ul>
                </template>
                    
              
            </div>
        </div>
        <div class='index-right'>
            <div style="font-size:40px;text-align:center;line-height:300px;width:900px;height:300px;background:red;margin:0 auto;">slider</div>
            <div class='index-board-list'>
                <div class='index-board-item'>
                    <div class='index-board-item-inner'>
                        <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好哇</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
                <div class='index-board-item'>
                    <div class='index-board-item-inner'>
                         <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好哇</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
                <div class='index-board-item'>
                    <div class='index-board-item-inner'>
                         <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好哇</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
                <div class='index-board-item'>
                    <div class='index-board-item-inner'>
                         <h2>戴尔电脑</h2>
                        <p>戴尔电脑就是好哇</p>
                        <div class='index-board-button'>立即购买</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
    productList: {
         pc: {
          title: "PC产品",
          list: [
            {
              title: "数据统计",
              url: "http://starcraft.com"
            },
            {
              title: "数据预测",
              url: "http://warcraft.com"
            },
            {
              title: "流量分析",
              url: "http://overwatch.com",
              hot: true
            },
            {
              title: "广告发布",
              url: "http://hearstone.com"
            }
          ]
        },
        app: {
          title: "手机应用类",
          last:true,
          list: [
            {
              title: "91助手",
              url: "http://weixin.com"
            },
            {
              title: "产品助手",
              url: "http://weixin.com",
              hot:true
            },
            {
              title: "智能地图",
              url: "http://maps.com"
            },
            {
              title: "语音助手",
              url: "http://phone.com",
              hot:true
            }
          ]
        },
       
      },
    mess_new:{
            list_new:[
            {title:'如果王仙芝还活着，徐凤年就不是天下第一'},
            {title:'因为有邓太阿的存在，徐凤年也不能称为天下第一'},
            {title:'北莽还有武神拓跋菩萨，实力可能会随时超过徐凤年'}
                ] 
        }
    }
  },

}
</script>

<style scoped>
    .index-wrapper{
        width: 1200px;
        margin: 0 auto;
        display: flex;
    }
    .index-left{
        width:298px;
        /* border:1px solid black; */
    }
    .index-right{
        width: 900px;
    }
    .index-left-block{
        margin:15px;
        background:#fff;
        box-shadow: 0 0 1px #ddd;
        border-radius: 0 0 10px 10px;
    }
    .index-left-block h2{
        color:#fff;
        background: rgb(137, 216, 18);
        padding: 10px 15px;
        margin-bottom: 15px;
    }
    .all-products h3{
        padding: 0 15px 5px 15px;
        font-weight: bolder;
        color: #222;
    }
    .index-left-block ul{
        padding: 10px 15px;
    }
    .index-left-block li{
        padding: 5px;
    }
    .hot-tag {
       background: violet;
       color: white;
       font-size: 12px;
    }
    .index-board-list{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .index-board-item{
        width: 400px;
        background: white;
        box-shadow: 0 0 1 #ddd;
        margin-bottom: 20px;
        padding-top: 20px;
    }
    .index-board-item-inner{
        height: 125px;
        padding-left: 120px;
        background: url('../assets/logo.png');
        background-repeat: no-repeat;
        background-size: 23%;
        background-position: 23px;
    }
    .index-board-item-inner h2{
        font-size: 18px;
        font-weight: bolder;
        color: #000;
        margin-bottom: 15px;
    }
    .index-board-item-inner p{
        margin-bottom: 15px;
    }
    .index-board-button{
        width: 80px;
        height: 30px;
        line-height: 30px;
        border-radius: 5px;
        background: green;
        color:#fff;
        text-align: center
    }
</style>
    
