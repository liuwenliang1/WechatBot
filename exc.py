# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-16 13:34
e-mail: chuanwusun at gmail.com
"""
from enum import Enum


class TinkerErrorCode(Enum):

    MISSING_PARAMETER = 0


TRANSLATIONS = {
    TinkerErrorCode.MISSING_PARAMETER : u'缺少参数'
}


class TinkerSystemException(Exception):

    def __init__(self, err_code, err_msg=None):
        self.err_code = err_code
        self.err_msg = err_msg
    def __str__(self):
        print repr(self.err_code, self.err_msg if self.err_msg else
            TRANSLATIONS[self.err_msg])


def generate_user_exc(err_code, err_msg=None):
    """ Generate UserException which error message shall be show to user.

    :param err_code: Error code
    :return: UserException instance
    """
    return TinkerSystemException(err_code, err_msg)
