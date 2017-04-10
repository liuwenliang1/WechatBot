# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-12 16:01
e-mail: chuanwusun at gmail.com
"""
from tinker import r
from tinker.redis_utils import redis_client

TASK_KEY = 'TODO'


@r.register('add')
def add(task_detail):
    redis_client.zadd(TASK_KEY, 10, task_detail)
    return 'got it'


@r.register('list')
def get_task_list():
    result = ''
    for index, value in enumerate(redis_client.zrange(TASK_KEY, 0, -1)):
        result += '{}. {} \n'.format(index+1, value)
    return result


@r.register('kill')
def kill_task(task_id):
    result = {}
    for index, value in enumerate(redis_client.zrange(TASK_KEY, 0, -1)):
        result[index+1] = value
    redis_client.zrem(TASK_KEY, result[int(task_id)])
    return 'well done!'


if __name__ == '__main__':
    print add('test_1')
    print get_task_list()
    print kill_task(1)
    print get_task_list()
