# -*- coding:utf-8 -*-
from tinker import r


@r.register('ping')
def ping():
    """ tinker will reply pong after receiving !ping
        all commands should start with !
    """
    return 'pong'

