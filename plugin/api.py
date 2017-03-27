# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-15 08:23
e-mail: chuanwusun at gmail.com
"""
from flask_restful import Resource

from tools import get_v2ex


class V2EX(Resource):
    def get(self):
        return get_v2ex()
