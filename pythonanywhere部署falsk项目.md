## pythonanywhere部署falsk项目

### 1.注册账号

官网:pythonanywhere

![1586247360973](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247360973.png)****

![a'a](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247386094.png)





### 2.将github上的项目发送至pythonanywhere   

![1586246282329](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246282329.png)

![1586246353082](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246353082.png)

``` py
 git clone https://github.com/chao-yuan-cy/flask.git
```

![1586246440698](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246440698.png)

创建虚拟环境

``` python
virtualenv --python=python3.7 Flask_env
```

激活虚拟环境

``` python
source Flask_env/bin/activate
```

下载依赖

``` python
pip install -r requirements.txt 
#导出依赖命令
pip freeze > ./requirements.txt
```





创建web应用

![1586246734436](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246734436.png)

第一行项目路径

第二行家目录路径

![1586246829755](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246829755.png)

虚拟环境路径

![1586246886684](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246886684.png)

静态文件路径

![1586246924537](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246924537.png)

wsgi 配置

![1586247022191](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247022191.png)

![1586246972194](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586246972194.png)

from app import app as application

![1586247090017](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247090017.png)

刷新页面

![1586247145341](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247145341.png)

访问

![1586247183156](C:\Users\13371\AppData\Roaming\Typora\typora-user-images\1586247183156.png)