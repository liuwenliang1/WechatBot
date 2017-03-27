# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-03 13:59
e-mail: chuanwusun at gmail.com
"""
from tinker import r
from plugin import *


def parse_command(text):
    if text.startswith('!'):
        if ' ' in text:
            command, command_string = text[1:].split(' ', 1)
            return r.call_method(command, command_string)
        else:
            return r.call_method(text[1:])


if __name__ == '__main__':
    pass
