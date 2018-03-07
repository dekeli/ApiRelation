# coding=utf-8

"""
提取函数调用等运行时信息
"""
from apiCloud.cof.co_os import OsInfo

__author__ = 'Administrator'

import sys
import inspect
import traceback

import os
import re

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[%(lineno)d] %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.info(__name__)

cfgType = "dev"


class ExecHandler(object):
    """
    处理异常信息
    """


class Proc(object):
    def __init__(self):
        info = sys.exc_info()
        traceback.format_exc()
        pass

    def log_w(msg):
        f = inspect.currentframe()
        lineno = f.f_back.f_lineno

        if cfgType == "dev" or True:
            msg = "函数：" + str(f.f_back.f_code.co_name) + "行号：" + str(lineno) + "\t消息：" + str(msg)

    def get_call_info(self, msg):
        msg = sys._getframe().f_code.co_name + ': ' + msg
        return msg


class CoProc(object):
    POPEN = 1
    CALL = 2
    PROCESS = 3

    def __init__(self, t=PROCESS, debug=0):
        self.ty = t
        self.debug = debug

    def run(self, cmd):
        """
        运行程序

        :return:
        """

        retn = dict()
        logger.info(cmd)

        if self.ty == self.PROCESS:
            import subprocess

            if not self.debug:
                sub2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                retn['error'] = sub2.stderr.read()
                retn['result'] = sub2.stdout.read()
            else:
                logger.info(cmd)
        elif self.ty == self.CALL:
            os.system(cmd)
        elif self.ty == self.POPEN:
            fp = os.popen(cmd)
            retn['result'] = fp.read()

        return retn


def get_proc_list(proc_name):
    proc_o = CoProc(debug=False)

    oinfo = OsInfo()

    if oinfo.is_linux():
        res = proc_o.run("ps aux | grep %s" % proc_name)
    else:
        raise Exception("windows暂不支持该函数")

    logger.info(res)

    proc_list = list()

    res = res['result']
    res_list = res.split('\n')

    filter_str = 'grep %s' % proc_name

    def is_grep(s):
        if s.find(filter_str) != -1:
            return True
        else:
            return False

    for res in res_list:
        if len(res) > 0 and not is_grep(res):
            proc_list.append(res)

    logger.info(proc_list)

    return proc_list


def get_proc_count(proc_name):
    proc_list = get_proc_list(proc_name)
    return len(proc_list)


def get_proc_ids(proc_name):
    proc_ids = list()
    proc_list = get_proc_list(proc_name)
    patn = re.compile(r'\s+')
    if len(proc_list) > 0:
        for proc in proc_list:
            proc_info = patn.split(proc)
            if len(proc_info) > 1:
                proc_ids.append(int(proc_info[1]))

    return proc_ids


def kill_procs(proc_name):
    proc_ids = get_proc_ids(proc_name)
    logger.info("杀死进程 %s" % proc_name)
    logger.info(proc_ids)

    proc_o = CoProc(debug=0)

    for proc_id in proc_ids:
        cmd = 'kill -9 %s' % proc_id
        proc_o.run(cmd)


def get_proc_id(name):
    cmd = 'ps aux | grep \'%s\'' % name

    f = os.popen(cmd)

    info = f.read()

    # print "进程查询信息：" + cmd
    # print info
    procList = info.split("\n")
    # print procList
    for proc in procList:
        # print proc
        patn = re.compile(r'\s+')
        procInfo = patn.split(proc)
        # print len(procInfo)
        if len(procInfo) >= 10:
            # print "进程信息"
            cmdRun = procInfo[10]
            patn1 = re.compile(r'^grep')
            patn2 = re.compile(r'^sh')
            if not patn1.match(cmdRun) and not patn2.match(cmdRun):
                return procInfo[1]

    # print "进程不存在"
    return 0

    m = re.search('\w+\s+(\d+).*', info)
    # print m

    if m is not None:
        match = m.group()
        # print "匹配成功"
        # print match
        # print "分组"
        # print m.groups(0)
        if match.find("ps aux") > 0:
            # print "进程不存在"
            # print match.find("ps aux")
            return 0
        else:
            return m.groups(0)[0]


if __name__ == "__main__":
    proc = Proc()
    # print proc.get_call_info("hello, world")
    # print get_proc_id('log_server')
    try:
        raise Exception("hello, exeception")
    except Exception, err_msg:
        # print Exception
        # print err_msg
        # print str(err_msg)
        pass