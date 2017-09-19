# -*- coding:utf-8 -*-
import Queue
from wechatbot.bot import WechatBot

q = None


def get_msg_queue():
    global q
    if q is None:
        q = Queue.Queue()
    return q
