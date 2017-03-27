# Tinker
![tinker](https://travis-ci.org/chuanwu/Tinker.svg?branch=master)

*Tinker* is a wechat bot built for chatops. 


### Feature

- [x] 群消息回复
- [x] 联系人消息回复
- [ ] 命令支持正则匹配
- [ ] cron消息提醒
- [ ] @某人或者全部


### Quick Start

1. 安装pip

2. 安装依赖并运行测试脚本

   ```
   make test
   ```

3. 启动bot

   ```
   make mybot
   ```

4. 查看更多选项

   ```
   make help
   ```

5. 功能开发

 将你所实现的程序放到plugin/目录下，并使用该装饰器即可。

 ```
 @r.register('COMMAND_STRING')
 ```

 具体细节请看`plugin/ping_demo.py`。

### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).

### Usage

![WeChat](https://ooo.0o0.ooo/2017/03/21/58d00a410a12d.jpeg)
