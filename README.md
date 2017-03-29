# Tinker
![tinker](https://travis-ci.org/chuanwu/Tinker.svg?branch=master)

*Tinker* is a wechat bot built for geeeeeeeeks. 

### Quick Start

1. 安装依赖并运行测试脚本

   ```
   make test
   ```

2. 启动bot

   ```
   make mybot
   ```
   扫描二维码之后，机器人就跑起来啦。这时，可以向机器人发送一个!ping的消息来看看服务是否正常。

   ![Wechat](https://ooo.0o0.ooo/2017/03/29/58db399dd2ca6.jpeg)

3. 功能开发

 将你所实现的程序放到plugin/目录下，并使用该装饰器即可。

 ```
 @r.register('COMMAND_STRING')
 ```

 具体细节请看`plugin/ping_demo.py`。
 
### Plugin List

1. 测试服务是否存活。

向机器人发送`!ping`的指令。

2. 基本的get，set

> 此功能在demo分支中。

![演示](https://ooo.0o0.ooo/2017/03/30/58dbea829889a.jpeg)

3. 简单的任务管理

> 此功能在demo分支中。

![演示](https://ooo.0o0.ooo/2017/03/30/58dbea9f642d9.jpeg)


### Plan

目前主要分为三个分支来开发。

 * master
 
最稳定分支，但只包含一个测试bot是否正常运行的功能。
 
 * develop

开发分支，包含一些新增功能，但是不保证版本稳定。

 * demo
 
这是`chuanwu`自行开发的一些实际使用的功能，plugin列表会维护在master分支下的README。
 

### Feature

- [x] 群消息回复
- [x] 联系人消息回复
- [x] 增加一个todo list的plugin

### ToDo

- [ ] 命令支持正则匹配
- [ ] cron消息提醒
- [ ] @某人或者全部

### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).



In the end, thanks to [@elezhangwen](https://github.com/elezhangwen).
