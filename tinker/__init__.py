# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-10 22:25
e-mail: chuanwusun at gmail.com
"""
import logging
import sys

logger = logging.getLogger("Tinker")
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler("tinker.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
# print log to file and console
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
