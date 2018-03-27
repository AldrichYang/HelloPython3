# coding=utf-8


def estimate_hours_by_pages(pages=0, metrics=10):
    """ 估算一本技术书籍的阅读时间
       :param pages: 页数
       :param metrics: 度量标准，默认30分钟读10页
       :return: 小时数
       """
    return float(pages) / metrics * 30 / 60


def cost_time(book_dict, metrics=10):
    """
    计算每一本书籍的阅读小时数
    :param book_dict:书籍字典
    :param metrics:每30分钟读书页数
    :return:
    """
    total_hours = 0
    for k, v in book_dict.items():
        each_cost_hours = estimate_hours_by_pages(v, metrics)
        total_hours += each_cost_hours
        print(" {} estimate reading time is: {} hours".format(k, each_cost_hours))
    return total_hours


def cost_days(hours, week_day_reading_time=1.5):
    """
    基于某个度量计算总阅读天数
    :param hours:小时数
    :param week_day_reading_time:每天读书小时数
    :return:
    """
    print(" take {} days when cost {} hours each day ".format(round(hours / week_day_reading_time, 1),
                                                              week_day_reading_time))
