# coding=utf-8

"""
httplib的一层封装，更易于使用

.. doctest::

    >>> http_obj = cofHttp.Http(url, 80)
    >>> http_obj.set_header(header)
    >>> http_obj.post
"""

import time
import datetime
import urllib
import httplib
import json

__author__ = 'Administrator'

IMPORTLIB = False
REPEAT_TIMES = 1


def get_current_time():
    """
    获取当前时间
    """
    current_time = int(time.time()) * 1000 + datetime.datetime.now().microsecond / 1000
    return current_time


def send_url_using(url):
    """
    向测试管理平台发送当前接口测试请求的url(不包括协议，host和port)
    """
    host = 'plot.qa.sdp.nd'
    testing_platform_url = '/api/v1.0/api-url'
    method = 'POST'
    headers = dict()
    body = {
        'url': str(url)
    }
    body = json.dumps(body)

    flag = False

    conn = None

    try:
        conn = httplib.HTTPConnection(host)
        conn.request(method, testing_platform_url, body, headers)
        response = conn.getresponse()
        if response.status == 200:
            flag = True
    except Exception, e:  # 连接错误 or 读取错误
        # print 'error : ', str(e)
        pass

    if conn is not None:
        conn.close()


def send_host_port_using(host, port):
    """
    向测试管理平台发送当前接口测试请求的host和port，如果已经请求过了，就不会再发送
    :param host:
    :param port:
    :return:
    """
    if not host_port_is_used(host, port):
        host_platform_host = 'plot.qa.sdp.nd'
        testing_platform_url = '/api/v1.0/api-statis'
        method = 'POST'
        headers = dict()
        if port is not None:
            body = {
                'host': str(host),
                'port': long(port)
            }
        else:
            body = {
                'host': str(host),
                'port': 80
            }
        body = json.dumps(body)

        for index in range(REPEAT_TIMES):  # 三次重试
            flag = False
            conn = None
            try:
                conn = httplib.HTTPConnection(host_platform_host)
                conn.request(method, testing_platform_url, body, headers)
                response = conn.getresponse()
                if response.status == 200:
                    flag = True
                    # else:
                    #     print '给测试管理平台发送"' + str(host) + ':' + str(port) + '"失败'
            except Exception, e:  # 连接错误 or 读取错误
                # print 'error : ', str(e)
                pass
            if conn is not None:
                conn.close()
            if flag:
                break


def host_port_is_used(host, port):
    """
    查询测试管理平台，指定的主机和端口是否已被请求过
    :param host:
    :param port:
    :return:
    """
    is_used = False  # 返回host:port是否已被请求过
    host_platform_host = 'plot.qa.sdp.nd'
    testing_platform_url = '/api/v1.0/api-statis?host=' + str(host)
    method = 'GET'
    headers = dict()
    body = None

    for index in range(REPEAT_TIMES):  # 三次重试
        flag = False
        conn = None
        try:
            conn = httplib.HTTPConnection(host_platform_host)
            conn.request(method, testing_platform_url, body, headers)
            response = conn.getresponse()
            if response.status == 200:
                data = response.read()  # 响应的返回值
                data = json.loads(data)
                for item in data:
                    if item['host'] == host and item['port'] == port:
                        is_used = True
                        break
            flag = True
        except Exception, e:  # 连接错误 or 读取错误
            # print 'error : ', str(e)
            pass
        if conn is not None:
            conn.close()
        if flag:
            break

    return is_used


class Http(object):
    """对GET/POST进行了封装，让代码更简短易读
    :class:`cof.http.Http` 先初始化

    * `METHOD`: 默认请求方法
    """
    DEBUG = False

    METHOD = "GET"

    def __init__(self, host, port=None, ssl=False):
        """
        使用httplib库进行操作
        """
        self.host = host
        self.header = dict()
        self.params = None

        # 端口处理+（url）请求前缀拼装
        self.port = port
        if ssl:
            # 未指定端口，则使用默认端口
            if self.port is None or self.port == '':
                self.port = 443
            self.url_prefix = "https://" + str(host) + ':' + str(self.port)
            self.conn = httplib.HTTPSConnection(self.host, self.port)
        else:
            if self.port is None or self.port == '':
                self.port = 80
            self.url_prefix = "http://" + str(host) + ':' + str(self.port)
            self.conn = httplib.HTTPConnection(self.host, self.port)

            # self.test_manager = TestManager(20)

    def parse_url(self):
        pass

    def set_header(self, header):
        """
        设置http请求头，可以设置AccessToken等
        """
        self.header = header

    def send_request(self, res, method, url, headers, body=None):
        """
        封装发送请求的过程
        """
        conn = self.conn
        flag = False
        begin_time = 0
        end_time = 0

        try:
            begin_time = get_current_time()
            # 默认请求的url参数值中没有以下特殊字符
            # 可支持中文、特殊字符编码前后的情况
            url_transformed = urllib.quote(str(url), safe='$,-,_,.,+,!,*,(,),&,/,:,;,=,?,@,#,%')
            conn.request(method=method, url=url_transformed, headers=headers, body=body)
            response = conn.getresponse()
            end_time = get_current_time()

            # 状态码
            res["code"] = response.status

            # 响应的返回值
            res_data = response.read()
            res["data"] = res_data
            try:        # 如果响应内容是json格式，则先转成dict，再处理下中文转成str
                res_data_dict = json.loads(res_data)
                res_data = json.dumps(res_data_dict, ensure_ascii=False)
                res["data"] = res_data
            except Exception, e:
                pass

            # 响应的头信息
            res["response_header"] = response.msg.dict

            cookie = response.getheader("set-cookie")

            if cookie is not None:
                start = cookie.find("JSESSIONID=")
                end = cookie.find(";", start + 11)
                jsession = str(cookie[start + 11:end])
                res['jsession'] = jsession

            flag = True

        except Exception, e:  # 连接错误 or 读取错误
            if end_time == 0:
                end_time = get_current_time()
            res["code"] = 0

            # 响应的返回值
            res["data"] = '{}'

            # 响应的头信息
            res["response_header"] = dict()

        # http响应的间隔时间，单位ms
        res["response_time"] = end_time - begin_time

        conn.close()
        return flag

    def send(self, method, url, params=None):
        """
        各种请求：GET/POST/PUT/PATCH/DELETE/OPTIONS...
        # 创建http对象
        >>> http_o = Http(host, port)
        # 执行请求
        >>> res = http_o.send(url)
        # 获取响应码
        >>> code = res['code']
        >>> data = res['data']
        # 如果是json的话，需要解码
        >>> data_dec = json_decode(data)
        :param method: 请求方法，str
        :param url: url，str， 仅host、port后面的部分
        :param params: body参数
        :return: 响应
        注：暂时只考虑application/json的情况
        """
        # 请求方法必须是全大写英文单词
        method = (method.upper()).strip()

        # body数据必须转成字符串再传入http请求
        # 不是str就进行dumps转换，若转换失败就直接str格式化
        try:
            if not isinstance(params, str) and not isinstance(params, unicode):
                params = json.dumps(params)
        except Exception as e:
            params = str(params)

        res = dict()
        res["request"] = method + ' ' + self.url_prefix + url
        if params is not None and params != '':
            res["request"] += ",\nbody=" + params
        for index in range(REPEAT_TIMES):  # 重试
            if self.send_request(res, method, url, self.header, body=params) is True:
                break

        return res

        # def upload_files(self, url_in, file_path, params):
        #     """
        #     文件上传的方法 - 目前仅拼装http协议的情况
        #
        #     参数：
        #
        #     :param url_in:         请求url
        #
        #     :param file_path:   文件路径，包含文件名
        #
        #     :param params:     上传文件需要带有的参数，字典格式
        #     """
        #     if self.port is None:
        #         url = "http://" + str(self.host) + str(url_in)
        #     else:
        #         url = "http://" + str(self.host) + ":" + str(self.port) + str(url_in)
        #     file_o = open(file_path, "rb")
        #     params["fileUpload"] = file_o
        #
        #     register_openers()
        #
        #     datagen, headers = multipart_encode(
        #         params
        #     )
        #     print datagen
        #     print headers
        #     print params
        #
        #     # 创建请求对象
        #     request_handle = urllib2.Request(url, datagen, headers)
        #
        #     res = dict()
        #
        #     res['request'] = "POST " + str(url)
        #
        #     begin_time = get_current_time()
        #
        #     try:
        #         # 实际执行请求并取得返回
        #         response_handle = urllib2.urlopen(request_handle)
        #         res['code'] = response_handle.code
        #         res['data'] = response_handle.read()
        #         read_time = get_current_time()
        #         # self.test_manager.send_host_port(self.host, self.port)
        #         # self.test_manager.send_url(url_in)
        #     except urllib2.HTTPError as e:
        #         res['code'] = e.code
        #         res['data'] = e.read()
        #         read_time = get_current_time()
        #
        #     res["response_time"] = read_time - begin_time   # 单位ms
        #
        #     file_o.close()
        #
        #     return res

        # def upload_files(self, url_in, file_path, params):
        #     """
        #     文件上传的方法 - 目前仅拼装http协议的情况
        #
        #     参数：
        #
        #     :param url_in:         请求url
        #
        #     :param file_path:   文件路径，包含文件名
        #
        #     :param params:     上传文件需要带有的参数，字典格式
        #     """
        #     if self.port is None:
        #         url = "http://" + str(self.host) + str(url_in)
        #     else:
        #         url = "http://" + str(self.host) + ":" + str(self.port) + str(url_in)
        #     file_o = open(file_path, "rb")
        #     params["fileUpload"] = file_o
        #
        #     register_openers()
        #
        #     datagen, headers = multipart_encode(
        #         params
        #     )
        #     print datagen
        #     print headers
        #     print params
        #
        #     # 创建请求对象
        #     request_handle = urllib2.Request(url, datagen, headers)
        #
        #     res = dict()
        #
        #     res['request'] = "POST " + str(url)
        #
        #     begin_time = get_current_time()
        #
        #     try:
        #         # 实际执行请求并取得返回
        #         response_handle = urllib2.urlopen(request_handle)
        #         res['code'] = response_handle.code
        #         res['data'] = response_handle.read()
        #         read_time = get_current_time()
        #         # self.test_manager.send_host_port(self.host, self.port)
        #         # self.test_manager.send_url(url_in)
        #     except urllib2.HTTPError as e:
        #         res['code'] = e.code
        #         res['data'] = e.read()
        #         read_time = get_current_time()
        #
        #     res["response_time"] = read_time - begin_time   # 单位ms
        #
        #     file_o.close()
        #
        #     return res
