# coding=utf-8
from estimateDoTime import estimate_time as est


def add_recently_books():
    """
    add books
    :return:
    """
    books = dict()
    books['Redis实战'] = 270
    books['Zookeeper技术详解'] = 200
    books['SpringCloud实战'] = 417
    books['聊聊架构'] = 230
    books['Http权威指南'] = 518
    return books


cost_hours = est.cost_time(add_recently_books())
est.cost_days(cost_hours)
