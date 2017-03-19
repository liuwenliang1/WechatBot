# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-10 19:41
e-mail: chuanwusun at gmail.com
"""
import unittest

from core import (
    ping
)

class Ping(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(ping(), 'pong')

if __name__ == '__main__':
    pass
