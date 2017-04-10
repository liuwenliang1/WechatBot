# WechatBot
[![Build Status](https://travis-ci.org/chuanwu/WechatBot.svg?branch=master)](https://travis-ci.org/chuanwu/WechatBot)
[![codecov](https://codecov.io/gh/chuanwu/WechatBot/branch/master/graph/badge.svg)](https://codecov.io/gh/chuanwu/WechatBot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Tinker* is a wechat bot built for chatops.

### Quick Start

0. 支持pip安装

```
    pip install wechatbot
```

该功能尚在开发，还不成熟。请看1。
 

1. install dependency and run tests


[![Build Status](https://travis-ci.org/chuanwu/WechatBot.svg?branch=master)](https://travis-ci.org/chuanwu/WechatBot)

   ````
   make test
   ```

2. 启动bot

   ```
   make mybot
   ```
   扫描二维码之后，机器人就跑起来啦。
   这时，可以向机器人发送一个!ping的消息来看看服务是否正常。

   ![Ping](https://ooo.0o0.ooo/2017/03/29/58db399dd2ca6.jpeg)

3. 定制功能

接入更多功能，你可以在你的函数上加上这个

 ```
 @r.register('COMMAND_STRING')
 ```

 可以参考 `plugin/ping_demo.py`。


### 规划

接下来会把Bot做成一个更加基础的服务，只对外暴露三个模块，

1. 在接受指令之后发送定制消息

后续会增加session的概念，可能会支持AI，并通过向机器人发送消息来开关AI。
来自用户的每一条消息都是作为一个命令。

2. 主动向某个用户发送消息


### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).


In the end, thanks to [@elezhangwen](https://github.com/elezhangwen).
