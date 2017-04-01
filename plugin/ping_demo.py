# -*- coding:utf-8 -*-
from tinker import r


@r.register('ping')
def ping():
    """ 机器人将在接受到!ping的消息后，返回pong
        对机器人的所有命令均以!开头
    """
    return 'pong'
