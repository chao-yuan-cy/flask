### Cmder安装及配置

简介
与 Windows 自带的 cmd 和 PowerShell 相比，cmder 具有友好的界面和更加丰富的功能。

安装
下载地址：http://cmder.net/

解压后，得到 cmder 文件夹。将其拷贝到 D:\Program Files\ 目录下。

然后，将 Cmder.exe 所在的目录（D:\Program Files\cmder），添加至 Windows 系统的环境变量。

配置以管理员身份运行 Cmder
找到 Cmder.exe 的保存路径，右键 Cmder.exe ，属性→兼容性，勾选 【 以管理员身份运行此程序 】，确认保存。

这样，每次运行 Cmder 时，就都是以管理员的身份执行的。

之后，就可以使用 Win + R，输入 cmder，来打开 cmder 命令行界面。

注册到右键菜单

以管理员身份运行终端，执行下面的命令即可。

Cmder.exe /REGISTER ALL

执行成功的话，就可以在右键菜单中看到 Cmder Here 的选项。





 打开cmder，Win+Alt+p打开setting 



## 设置中文编码

 添加一行配置，然后保存 

```
set LANG=zh_CN.UTF8
```

 ![img](https://img-blog.csdnimg.cn/20190511225947698.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2d1aWt1bmNoZW4=,size_16,color_FFFFFF,t_70) 

## 防止字体重叠

 把这个勾去掉就好了 

 ![img](https://img-blog.csdnimg.cn/20190511230155690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2d1aWt1bmNoZW4=,size_16,color_FFFFFF,t_70) 