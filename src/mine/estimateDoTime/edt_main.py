# coding=utf-8
from mine.estimateDoTime import estimate_time as est


def add_it_books():
    """
    add books
    :return:
    """
    books = dict()
    books['Redis实战'] = 270
    books['Zookeeper技术详解'] = 200
    books['SpringCloud实战'] = 417
    books['聊聊架构'] = 230
    # books['Http权威指南'] = 518
    books['高性能Mysql'] = 800
    books['Netty权威指南'] = 526
    return books


def add_it_en_books():
    """
    网络教程：每一章当做中文30分钟的页数
    英文书籍：每一页乘以2，当做中文页数
    """
    en_books = dict()
    # en_books['Java IO'] = 17 * 10
    # en_books['Java Network'] = 22 * 10
    en_books['Java Servlet'] = 240 * 2
    return en_books


def add_finished_readings():
    finished_readings = [
        'Java IO',
        'Java Network'
    ]
    return finished_readings


cost_hours = est.cost_time(add_it_books())
cost_hours += est.cost_time(add_it_en_books())
est.cost_days(cost_hours)
