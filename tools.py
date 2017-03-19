# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-15 14:15
e-mail: chuanwusun at gmail.com
"""
import json

import editdistance

from spiders.v2ex import fetch_v2ex
from models import redis_client

def update_v2ex():
    key = 'v2ex'
    result =  fetch_v2ex()
    for r in result:
        data = {'title': r['title'], 'url': r['url']}
        print redis_client.lpush(key, json.dumps(data))

def get_v2ex():
    key = 'v2ex'
    ret = list()
    result = redis_client.lrange(key, 0, 20)
    for r in result:
        ret.append(json.loads(r))
    return ret


def get_hacker():
    key = 'hacker'
    ret = list()
    result = redis_client.lrange(key, 0, 20)
    for r in result:
        ret.append(json.loads(r))
    return ret

def refresh():
    redis_client.flushall()
    update_v2ex()

def calc_str_distance(command, candidate):
    """ Calculates the distance between two strings
        ref: Levenshtein Distance
    """
    return editdistance.eval(command, candidate)

def guess(command, candidates):
    holy_table = {}
    for candidate in candidates:
        holy_table[candidate] = calc_str_distance(command, candidate)
    sorted_command = sorted(holy_table.iteritems(), key=lambda (k,v): (v,k))
    return sorted_command[0][0]

if __name__ == '__main__':
    pass
