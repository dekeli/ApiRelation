# coding=utf-8

__author__ = 'linzh'

import os
import nd


class NdPath(object):
    """
    路径解析
    """
    def __init__(self):
        pass

    @staticmethod
    def get_jlib_path():
        """
        获取jlib路径

        md5.jar:
        token.jar

        :return:
        """
        # return nd.__path__[0] + os.sep + 'jlibs' + os.sep
        current_dir = os.path.dirname(os.path.realpath(__file__))  # 当前文件所在目录
        return current_dir + os.sep + 'jlibs' + os.sep



