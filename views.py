# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-15 08:23
e-mail: chuanwusun at gmail.com
"""
from flask import render_template
from flask_restful import Resource

from models import redis_client
from consts import ALL_KEYWORDS

class HelloWorld(Resource):
    def get(self):
        page_name = 'index'
        keywords = redis_client.smembers(ALL_KEYWORDS)
        return render_template('%s.html' % page_name, keywords = keywords)
