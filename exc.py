# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-16 13:34
e-mail: chuanwusun at gmail.com
"""
from enum import Enum


class TinkerErrorCode(Enum):

    MISSING_PARAMETER = 0
    UNKNOWN_COMMAND = 1
    RESERVED_COMMAND = 2
    DUPLICATED_COMMAND = 3
    SEND_MSG_ERROR = 4
    LOGIN_ERROR = 5
    GET_UUID_ERROR = 6
    SYNC_ERROR = 7
    SYNC_CHECK_ERROR = 8
    SYNC_HOST_CHECK_ERROR = 9
    BOT_INIT_ERROR = 10


TRANSLATIONS = {
    TinkerErrorCode.MISSING_PARAMETER: u'you may omit some parameter',
    TinkerErrorCode.UNKNOWN_COMMAND: u'sorry, i can not understand.',
    TinkerErrorCode.RESERVED_COMMAND: u'sorry, this command is a reserved keyword.',
    TinkerErrorCode.DUPLICATED_COMMAND: u'duplicate command.',
    TinkerErrorCode.SEND_MSG_ERROR: u'failed to send msg',
    TinkerErrorCode.LOGIN_ERROR: u'failed to login',
    TinkerErrorCode.GET_UUID_ERROR: u'failed to get uuid',
    TinkerErrorCode.SYNC_CHECK_ERROR: u'failed to sync check',
    TinkerErrorCode.SYNC_HOST_CHECK_ERROR: u'failed to sync host check',
    TinkerErrorCode.BOT_INIT_ERROR: u'failed to init bot',
    TinkerErrorCode.SYNC_ERROR: u'failed to sync'
}


class TinkerException(Exception):

    def __init__(self, err_code, err_msg=None):
        self.err_code = err_code
        self.err_msg = err_msg

    def __str__(self):
        return repr(self.err_msg if self.err_msg else
                    TRANSLATIONS[self.err_code])


class TinkerUserExceptioin(TinkerException):
    pass


class TinkerSystemException(TinkerException):
    pass


class TinkerServerException(TinkerException):
    pass
