# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-12 16:01
e-mail: chuanwusun at gmail.com
"""
from tinker import r


@r.register('rmb')
def rmb(args):
    """Convert rmb to pound
    """
    return round(int(args) / 8.5, 2)


@r.register('pound')
def pound(args):
    """Convert pund to rmb
    """
    return int(args) * 8.5
