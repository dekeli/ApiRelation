# coding=utf-8


__author__ = ""

# 该模块封装属于当前服务的http基本操作
import json, urllib
import requests

from ..config_file.config_test import ConIni
from ..config_file import Consts

from ..config_file.config_test import ConIni



class BaseHttp(object):
    def __init__(self, env=None):
        """

        :param env: 指定配置文件中的环境名称
        """
        self.env = env

        # 读配置文件，获取host等配置
        my_cfg = ConIni.PPD[env]

        # 声明默认的http对象（声明后才有具体实例）、header（设置后才生效)等
        self.host = my_cfg["host"]

        self.header = my_cfg["header"]

        self.port = my_cfg["port"]

    def get_url(self, url):
        """

        :param url: url地址前加上"/"
        :return: url
        """
        if self.port:
            url = self.host + ":" + self.port + url
        else:
            url = self.host + url
        return url

    def get(self, url, params=None):
        url = self.get_url(url)
        headers = self.header
        try:
            if params is None:
                response = requests.get(url=url, headers=headers)
            else:
                response = requests.get(url=url, params=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post(self, url, params=None):
        url = self.get_url(url)
        headers = self.header
        try:
            if params is None:
                response = requests.post(url=url, headers=headers)
            else:
                response = requests.post(url=url, json=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts


    def patch(self, url, params=None):
        url = self.get_url(url)
        headers = self.header
        try:
            if params is None:
                response = requests.patch(url=url, headers=headers)
            else:
                response = requests.patch(url=url, params=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts



    def put(self, url, params=''):
        url = self.get_url(url)
        headers = self.header
        try:
            if params is None:
                response = requests.patch(url=url, headers=headers)
            else:
                response = requests.patch(url=url, params=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def delete_re(self, url, params=''):
        url = self.get_url(url)
        headers = self.header
        try:
            if params is None:
                response = requests.patch(url=url, headers=headers)
            else:
                response = requests.patch(url=url, params=params, headers=headers)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
