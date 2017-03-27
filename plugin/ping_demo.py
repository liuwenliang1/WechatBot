# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-12 16:01
e-mail: chuanwusun at gmail.com
"""
from tinker import r


@r.register('ping')
def ping():
    return 'pong'
