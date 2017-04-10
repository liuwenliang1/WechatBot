# -*- coding:utf-8 -*-
from wechatbot import r


def test_ping_case():
    assert r.call_method('ping') == 'pong'

if __name__ == '__main__':
    pass
