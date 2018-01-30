# coding=utf-8

import logging

# named the logger
logger = logging.getLogger('LazyLogging')
# 设置log level
logger.setLevel(logging.DEBUG)
# 指定输出目标
hander = logging.StreamHandler()
# 指定输出格式（时间，logger name，log level，具体的日志内容）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

hander.setFormatter(formatter)

logger.addHandler(hander)


def getUserCount():
    logger.info('getUserCount is called')

    return 1


logger.debug("There are " + str(getUserCount()) + " users logged in now.")
