# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-12 16:01
e-mail: chuanwusun at gmail.com
"""
from tinker import r
from tinker.redis_utils import redis_client


@r.register('get')
def get_value(key):
    return redis_client.get(key)


@r.register('set')
def set_value(args):
    if ' ' not in args:
        return 'syntax error.'
    key, value = args.split(' ', 1)
    redis_client.set(key, value)
    return 'got it'

if __name__ == '__main__':
    print set_value('test a dev.')
    print get_value('test')
