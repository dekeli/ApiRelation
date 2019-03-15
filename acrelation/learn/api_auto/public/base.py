# import  HttpService
from ..config_file import Config
from ..public import HttpService
from ..config_file import Config


# 拼接请求的url
class Base_Service(object):

    def __init__(self):
        pass

    def get_url(Endurl):
        host = Config.host()
        url = Endurl
        port = Config.port()
        if port == '':
            url = ''.join([host, url])
            return url
        url = host + ":" + port + url
        print('11111'+url)


    # # 获取请求的方式
    # def get_req_way(url, Method, **DataALL):
    #     if Method == 'get':
    #         resp = HttpService.MyHttp().get(url, **DataALL)
    #     elif Method == 'post':
    #         resp = HttpService.MyHttp().post(url, **DataALL)
    #     elif Method == 'put':
    #         resp = HttpService.MyHttp().put(url, **DataALL)
    #         return resp

import requests


class MyHttp(object):
    def __init__(self):
        pass


    #封装请求方法
    def get(self, url, **DataALL):
        """
        :param url: 请求的url
        :param DataALL: 存放请求参数，包括headers、json等
        :return: text
        """
        params = DataALL.get('params')
        params = DataALL.get('headers')
        try:
            resp = requests.get(url, params=params)
            text = resp.json()
            return text
        except Exception as e:
            print('get错误： %s' %e)

    def post(self, url, **DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        data = DataALL.get('data')
        json = DataALL.get('json')
        try:
            resp = requests.post(url, params=params)
            text = resp.json()
            return text
        except Exception as e:
            print('post错误：%s' %e)

    def put(self, url, **DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        data = DataALL.get('data')
        json = DataALL.get('json')
        resp = requests.put(url, params=params)
        text = resp.json()
        return text
