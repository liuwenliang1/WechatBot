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

### Feature

- [ ] 群消息回复
- [ ] 联系人消息回复

### TODO

- [ ] 命令支持正则匹配
- [ ] cron消息提醒
- [ ] @某人或者全部
- [ ] 增加一个todo list的plugin

### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).



In the end, thanks to [@elezhangwen](https://github.com/elezhangwen).