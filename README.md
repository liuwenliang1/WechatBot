# Tinker

*Tinker* is a wechat bot built for chatops. 

### Feature

- [x] 群消息回复
- [x] 联系人消息回复
- [ ] 命令支持正则匹配

### Quick Start

1. 安装pip

   如果已经安装pip，请跳至第二步

   - Mac

     ```
     easy_install pip
     ```

   - Ubuntu

     ```
     apt-get install python-pip python-dev build-essential
     ```

   - CentOS

     ```
     yum -y install python-pip
     ```

2. 安装并启动redis

   请按照该[文档](https://redis.io/topics/quickstart)安装redis。

3. 安装依赖

   ```
   make install
   ```

4. 配置main.ini

   ```
   cp example.main.ini main.ini
   # 请更新该配置文件
   vim main.ini
   ```

5. 启动bot

   ```
   make mybot
   ```

6. 查看更多选项

   ```
   make help
   ```

### Usage

![WeChat](https://ooo.0o0.ooo/2017/03/21/58d00a410a12d.jpeg)







