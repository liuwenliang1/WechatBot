# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-10 22:29
e-mail: chuanwusun at gmail.com
"""
import redis

import ConfigParser

config = ConfigParser.RawConfigParser()
try:
    config.read('main.ini')
    REDIS_HOST = config.get('redis', 'host')
except:
    config.read('example.main.ini')
    REDIS_HOST = config.get('redis', 'host')

REDIS_PASSWD = config.get('redis', 'passwd')
REDIS_PORT = config.get('redis', 'port')


redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=0,
    password=REDIS_PASSWD,
    socket_timeout=5,
    charset='utf-8',
    errors='strict'
)
