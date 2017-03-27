# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-03 13:59
e-mail: chuanwusun at gmail.com
"""
from tinker.redis_utils import redis_client
from tools import guess
from routing import Routing
from exc import TinkerUserExceptioin, TinkerErrorCode

r = Routing()


@r.register('ping')
def ping():
    return 'pong'


@r.register('help')
def get_help():
    return 'help'


@r.register('set')
def bot_set(command_string):
    if ' ' not in command_string:
        raise TinkerUserExceptioin(TinkerErrorCode.MISSING_PARAMETER)
    key, value = command_string.split(' ', 1)
    redis_client.set(key, value)
    return 'got it'


@r.register('get')
def get(key):
    if key not in redis_client.keys():
        return '{}? Or you mean {}?'.format(key, guess(key, redis_client.keys()))
    return redis_client.get(key)


def parse_command(text):
    if text.startswith('!'):
        if ' ' in text:
            command, command_string = text[1:].split(' ', 1)
            return r.call_method(command, command_string)
        else:
            return r.call_method(text[1:])


if __name__ == '__main__':
    pass
