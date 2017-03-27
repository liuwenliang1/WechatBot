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


TRANSLATIONS = {
    TinkerErrorCode.MISSING_PARAMETER: u'you may omit some parameter',
    TinkerErrorCode.UNKNOWN_COMMAND: u'sorry, i can not understand.',
    TinkerErrorCode.RESERVED_COMMAND: u'sorry, this command is a reserved keyword.'
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
