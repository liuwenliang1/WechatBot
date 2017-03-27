# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-15 14:15
e-mail: chuanwusun at gmail.com
"""
from consts import RESERVED_COMMAND_LIST
from exc import TinkerUserExceptioin, TinkerErrorCode

class Routing():
    def __init__(self):
        self.func_map = {}

    def register(self, routing_key):
        def func_wrapper(func):
            if routing_key in RESERVED_COMMAND_LIST:
                raise TinkerUserExceptioin(TinkerErrorCode.RESERVED_COMMAND)
            self.func_map[routing_key] = func
            return func
        return func_wrapper

    def call_method(self, command=None, *args, **kwargs):
        """Call method by command and msg

        :param command: the command you registered
        :param args:  the msg you passed on
        :param kwargs:
        :return:
        """
        return self.func_map[command](*args, **kwargs)
