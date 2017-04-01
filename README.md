# Tinker
![tinker](https://travis-ci.org/chuanwu/Tinker.svg?branch=master)

*Tinker* is a wechat bot built for chatops.

### Quick Start

1. install dependency and run tests

   ```
   make test
   ```

2. start bot

   ```
   make mybot
   ```
   Open url according to the hint and scan the qr code, Tinker starts running.
   After that, you can send a `!ping` to bot, Tinker will reply pong as response.

   ![Wechat](https://ooo.0o0.ooo/2017/03/29/58db399dd2ca6.jpeg)

3. more functions..

 Place your python files under plugin, and add the following decorator.

 ```
 @r.register('COMMAND_STRING')
 ```

 For more details, you may wanna read `plugin/ping_demo.py`。
 
### Plugin List

1. Test if bot is alive.

Send `!ping`.

2. redis-like get，set

> switch to demo branch and add your redis config in main.ini like example.main.ini

![demo](https://ooo.0o0.ooo/2017/03/30/58dbea829889a.jpeg)

3. todo list

> switch to demo branch and add your redis config in main.ini like example.main.ini

![demo](https://ooo.0o0.ooo/2017/03/30/58dbea9f642d9.jpeg)


### branches

 * master

 most stable branch. Strongly recommend to use this branch

 * develop

 just for developing

 * demo

 some plugins developed by chuanwu

### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).


In the end, thanks to [@elezhangwen](https://github.com/elezhangwen).
