# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-10 19:41
e-mail: chuanwusun at gmail.com
"""
from core import r
from exc import TinkerUserExceptioin


def test_ping_case():
    assert r.call_method('ping') == 'pong'


def test_set_get_case():
    assert r.call_method('set', 'author a dev') == 'got it'

    try:
        r.call_method('set', 'author') == TinkerUserExceptioin
    except TinkerUserExceptioin:
        pass


if __name__ == '__main__':
    pass
