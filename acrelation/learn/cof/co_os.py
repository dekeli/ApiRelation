# coding=utf-8

__author__ = 'linzh'

import platform


class OsInfo(object):
    @staticmethod
    def get_os():
        return platform.system().lower()

    @staticmethod
    def is_linux():
        if OsInfo.get_os() == "linux":
            return True
        else:
            return False


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(__name__)

    logger.info(OsInfo.get_os())
    logger.info(OsInfo.is_linux())
