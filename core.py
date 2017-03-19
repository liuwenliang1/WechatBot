# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-03-03 13:59
e-mail: chuanwusun at gmail.com
"""
import json

from flask import render_template
from flask_restful import Api

from wsgi import application
from views import HelloWorld
from spiders.api import V2EX
from models import redis_client
from consts import ALL_KEYWORDS
from tools import guess

api = Api(application)
api.add_resource(HelloWorld, '/')
api.add_resource(V2EX, '/v2ex')

@application.route("/")
def index():
    page_name = 'index'
    keywords = redis_client.smembers(ALL_KEYWORDS)
    return render_template('%s.html' % page_name, keywords = keywords)

func_map = {
    'ping': lambda args: ping(args),
    'set':  lambda args: set(args),
    'get':  lambda args: get(args),
    'v2ex': lambda args: v2ex(args),
    'hacker': lambda args: hacker(args)
}


def parse_command(text):
    if text.startswith('!'):
        text = text[1:]
        command, args = text.split(' ', 1) if ' ' in text else (text, '')
        print '\n'
        print text, command, args
        if command in func_map:
            return func_map[command](args)


def smembers(key):
    values = redis_client.smembers('key')
    text = ''
    if values:
        for i, value in enumerate(values):
            text += '{}. {}'.format(i, value)
    return text


def ping(args=None):
    return u'pong'

def set(args):
    if ' ' in args:
        key, value = args.split(' ', 1)
        redis_client.set(key, value)
        return 'got it'

def get(args):
    if args not in redis_client.keys():
        return '{}? Or you mean {}?'.format(args, guess(args, redis_client.keys()))
    return redis_client.get(args)

def v2ex(args):
    text = ''
    for topic in fetch_v2ex():
         text += '{} \n {}\n \n'.format(topic['title'].encode('utf-8'), topic['url'])
    return text

def hacker(args):
    text = ''
    for topic in fetch_hacker():
        text += '{} \n {}\n \n'.format(topic['title'].encode('utf-8'), topic['url'])
    return text

def fetch_v2ex():
    key = 'v2ex'
    ret = list()
    result = redis_client.lrange(key, 0, 20)
    for r in result:
        ret.append(json.loads(r))
    return ret

def fetch_hacker():
    key = 'hacker'
    ret = list()
    result = redis_client.lrange(key, 0, 20)
    for r in result:
        ret.append(json.loads(r))
    return ret

if __name__ == '__main__':
    import sys
    args = sys.argv
    application.run(host="0.0.0.0", port=args[1] if len(args) >= 2 else 5000)
