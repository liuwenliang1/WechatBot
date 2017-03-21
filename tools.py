# -*- coding:utf-8 -*-
"""
author: chuanwu.sun
created: 2017-02-15 14:15
e-mail: chuanwusun at gmail.com
"""
import editdistance

from models import redis_client

def calc_str_distance(command, candidate):
    """ Calculates the distance between two strings
        ref: Levenshtein Distance
    """
    return editdistance.eval(command, candidate)

def guess(command, candidates):
    holy_table = {}
    for candidate in candidates:
        holy_table[candidate] = calc_str_distance(command, candidate)
    sorted_command = sorted(holy_table.iteritems(), key=lambda (k,v): (v,k))
    return sorted_command[0][0]

if __name__ == '__main__':
    pass
